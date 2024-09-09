# import urllib.request
# import json
# import os
# import ssl

# def allowSelfSignedHttps(allowed):
#     # bypass the server certificate verification on client side
#     if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
#         ssl._create_default_https_context = ssl._create_unverified_context

# allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# # Request data goes here
# # The example below assumes JSON formatting which may be updated
# # depending on the format your endpoint expects.
# # More information can be found here:
# # https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
# while True:
#     query = str(input("enter input query: "))
#     data = {"query":query}

#     body = str.encode(json.dumps(data))

#     url = 'https://knowlegekeeperdemo-nnaek.eastus.inference.ml.azure.com/score'
#     # Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
#     api_key = 'u3hOLvUX9FXcLa9CC43LhYXz6t9atq8y'
#     if not api_key:
#         raise Exception("A key should be provided to invoke the endpoint")


#     headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

#     req = urllib.request.Request(url, body, headers)

#     try:
#         response = urllib.request.urlopen(req)

#         result = response.read()
#         result_json = json.loads(result.decode('utf-8'))
#         reply = result_json['reply']
#         print(reply)
#     except urllib.error.HTTPError as error:
#         print("The request failed with status code: " + str(error.code))

#         # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
#         print(error.info())
#         print(error.read().decode("utf8", 'ignore'))



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

    url = 'https://keeperproj-nfspj.eastus.inference.ml.azure.com/score'
    # Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
    api_key = 'NI7iEU0bE68rJQBHfEu7tHVk8e2X1kV9'
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
