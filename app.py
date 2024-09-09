# # Start by making sure the `assemblyai` package is installed.
# # If not, you can install it by running the following command:
# # pip install -U assemblyai
# #
# # Note: Some macOS users may need to use `pip3` instead of `pip`.

# import assemblyai as aai

# # Replace with your API key
# aai.settings.api_key = "1d890b82949b45bdbd455f728a38f88c"

# # URL of the file to transcribe
# FILE_URL = "C:\\Users\\akshay.bachkar\\OneDrive-Quorum Business Solutions\\Recordings\\WIN_20240801_10_13_42_Pro.mp4"

# # You can also transcribe a local file by passing in a file path
# # FILE_URL = './path/to/file.mp3'

# print('hello')

# transcriber = aai.Transcriber()
# transcript = transcriber.transcribe(FILE_URL)

# if transcript.status == aai.TranscriptStatus.error:
#     print(transcript.error)
# else:
#     print(transcript.text)

# import streamlit as st
# from streamlit_chat import message

# # Setting up the page configuration
# st.set_page_config(page_title="ChatGPT-like Chatbot", page_icon="🤖")

# # Title of the web app
# st.title("ChatGPT-like Chatbot 🤖")

# # Initialize session state variables for storing chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Function to simulate AI response
# def get_bot_response(user_input):
#     # For simplicity, we'll just echo the user input
#     # Replace this with a call to your AI model or API
#     return f"Bot: {user_input}"

# # Display the chat messages
# for i, (user_msg, bot_msg) in enumerate(st.session_state.messages):
#     message(user_msg, is_user=True, key=f"user_{i}")
#     message(bot_msg, key=f"bot_{i}")

# # Input box for user to type their message
# user_input = st.text_input("Type your message here...", key="user_input")

# # Handle user input submission
# if user_input:
#     # Append user message and bot response to session state
#     bot_response = get_bot_response(user_input)
#     st.session_state.messages.append((f"You: {user_input}", bot_response))
#     # Clear the input box after submission
#     st.session_state.user_input = ""

#     # Display the updated chat
#     for i, (user_msg, bot_msg) in enumerate(st.session_state.messages):
#         message(user_msg, is_user=True, key=f"user_{i}")
#         message(bot_msg, key=f"bot_{i}")


# import streamlit as st
# from streamlit_chat import message

# # Setting up the page configuration
# st.set_page_config(page_title="ChatGPT-like Chatbot", page_icon="🤖")

# # Title of the web app
# st.title("ChatGPT-like Chatbot 🤖")

# # Initialize session state variables for storing chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Function to simulate AI response
# def get_bot_response(user_input):
#     # For simplicity, we'll just echo the user input
#     # Replace this with a call to your AI model or API
#     return f"Bot: {user_input}"

# # Input box for user to type their message
# user_input = st.text_input("Type your message here...", key="input")

# # Handle user input submission
# if user_input:
#     # Append user message and bot response to session state
#     bot_response = get_bot_response(user_input)
#     st.session_state.messages.append((f"You: {user_input}", bot_response))

#     # Clear the input box by resetting its value to an empty string in session state
#     st.session_state["input"] = ""

# # Display the chat messages
# for i, (user_msg, bot_msg) in enumerate(st.session_state.messages):
#     message(user_msg, is_user=True, key=f"user_{i}")
#     message(bot_msg, key=f"bot_{i}")

import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

import streamlit as st
from streamlit_chat import message

# Setting up the page configuration
st.set_page_config(page_title="KnoledgeKeeper", page_icon="🤖")

# Title of the web app
st.title("KnoledgeKeeper 🤖")

# Initialize session state variables for storing chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to simulate AI response
def get_bot_response(user_input):
    # For simplicity, we'll just echo the user input
    # Replace this with a call to your AI model or API
    query = user_input
    data = {"query":query}

    body = str.encode(json.dumps(data))

    url = 'https://knowlegekeeperdemo-nnaek.eastus.inference.ml.azure.com/score'
    # Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
    api_key = 'u3hOLvUX9FXcLa9CC43LhYXz6t9atq8y'
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")


    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        result_json = json.loads(result.decode('utf-8'))
        reply = result_json['reply']
        # print(reply)
        return f"Bot: {reply}"
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))
    return f"Bot: {error.info()}"

# Input form for user to type their message
with st.form(key="input_form", clear_on_submit=True):
    user_input = st.text_input("Type your message here...", key="input")
    submit_button = st.form_submit_button(label="Send")

# Handle user input submission
if submit_button and user_input:
    # Append user message and bot response to session state
    bot_response = get_bot_response(user_input)
    st.session_state.messages.append((f"You: {user_input}", bot_response))

# Display the chat messages
for i, (user_msg, bot_msg) in enumerate(st.session_state.messages):
    message(user_msg, is_user=True, key=f"user_{i}")
    message(bot_msg, key=f"bot_{i}")


# import streamlit as st
# from streamlit_chat import message

# # Setting up the page configuration
# st.set_page_config(page_title="ChatGPT-like Chatbot", page_icon="🤖")

# # Title of the web app
# st.title("ChatGPT-like Chatbot 🤖")

# # Initialize session state variables for storing chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Function to simulate AI response
# def get_bot_response(user_input):
#     # For simplicity, we'll just echo the user input
#     # Replace this with a call to your AI model or API
#     return f"Bot: {user_input}"

# # Create a container for the chat messages with a scrollable view
# chat_container = st.container()
# input_container = st.container()

# # Display the chat messages
# with chat_container:
#     chat_container.markdown("<div style='height: 400px; overflow-y: auto;'>", unsafe_allow_html=True)
#     for i, (user_msg, bot_msg) in enumerate(st.session_state.messages):
#         message(user_msg, is_user=True, key=f"user_{i}")
#         message(bot_msg, key=f"bot_{i}")
#     chat_container.markdown("</div>", unsafe_allow_html=True)

# # Input box and send button are rendered at the bottom in a fixed container
# with input_container:
#     user_input = st.text_input("Type your message here...", key="input", label_visibility="collapsed")
#     submit_button = st.button("Send")

# # Handle user input submission
# if submit_button and user_input:
#     # Append user message and bot response to session state
#     bot_response = get_bot_response(user_input)
#     st.session_state.messages.append((f"You: {user_input}", bot_response))

#     # Clear the input field after submission
#     st.session_state["input"] = ""

# # Ensure the input box is fixed at the bottom
# st.markdown(
#     """
#     <style>
#     .block-container {
#         padding-top: 10px;
#         padding-bottom: 0px;
#     }
#     .stTextInput {
#         position: fixed;
#         bottom: 0;
#         width: 100%;
#     }
#     .stButton {
#         position: fixed;
#         bottom: 0;
#         right: 0;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
