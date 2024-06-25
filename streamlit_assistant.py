import streamlit as st
import json
import speech_recognition as sr
from io import BytesIO
import base64
import os
import requests
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema.messages import SystemMessage
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.tools import tool

load_dotenv()

class SearchTools:
    @tool("Search internet")
    def search_internet(query):
        """Useful to search the internet about a given topic and return relevant results."""
        return SearchTools.search(query)

    @staticmethod
    def search(query, n_results=5):
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        results = response.json().get('organic', [])
        string = []
        for result in results[:n_results]:
            try:
                string.append('\n'.join([
                    f"Title: {result['title']}", 
                    f"Link: {result['link']}",
                    f"Snippet: {result['snippet']}", 
                    "\n-----------------"
                ]))
            except KeyError:
                continue
        content = '\n'.join(string)
        return f"\nSearch result: {content}\n"

class Assistant:
    def __init__(self, model):
        self.chain = self._create_inference_chain(model)
        self.search_tools = SearchTools()

    def answer(self, prompt):
        if not prompt:
            return ""

        response = self.chain.invoke(
            {"prompt": prompt},
            config={"configurable": {"session_id": "unused"}},
        ).strip()

        # Check if the response indicates a need for internet search
        if "I need to search the internet" in response.lower():
            search_results = self.search_tools.search_internet(prompt)
            response += f"\n\nHere are some search results that might help:\n{search_results}"

        return response

    def _create_inference_chain(self, model):
        SYSTEM_PROMPT = """
        You are a witty assistant that will use the chat history to answer questions.
        If you don't know the answer, say "I need to search the internet for this information."
        Use few words on your answers. Go straight to the point. Do not use any
        emoticons or emojis. Do not ask the user any questions.
        Be friendly and helpful. Show some personality. Do not be too formal.
        """

        prompt_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=SYSTEM_PROMPT),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{prompt}"),
            ]
        )

        chain = prompt_template | model | StrOutputParser()

        chat_message_history = ChatMessageHistory()
        return RunnableWithMessageHistory(
            chain,
            lambda _: chat_message_history,
            input_messages_key="prompt",
            history_messages_key="chat_history",
        )

# Streamlit UI
st.title("AI Assistant with Voice and Text Input")

st.write("You can interact with the assistant using voice or text input.")

# Function to get speech input
def get_speech_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening... Speak now.")
        audio = r.listen(source)
        st.write("Processing speech...")
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        st.error("Sorry, I couldn't understand that. Please try again.")
    except sr.RequestError:
        st.error("Sorry, there was an error processing your speech. Please try text input.")
    return None

# Initialize Ollama with llama3:latest
@st.cache_resource
def load_model():
    return Ollama(model="llama3:latest")

model = load_model()
assistant = Assistant(model)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input method selection
input_method = st.radio("Choose input method:", ("Voice", "Text"))

prompt = None

if input_method == "Voice":
    if st.button("Start Voice Input"):
        prompt = get_speech_input()
        if prompt:
            st.write(f"You said: {prompt}")
    else:
        st.write("Click the button and start speaking when prompted.")
else:
    prompt = st.text_input("Type your question here:")

# Process input and generate response
if prompt:
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = assistant.answer(prompt)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.experimental_rerun()