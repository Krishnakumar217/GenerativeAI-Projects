import streamlit as st
import google.generativeai as genai

# Read the API Key and Setup a Gemini Client
with open(r"F:\Data Science\GenAI Stuffs\Projects\Python Code Reviewer\gemini_api_key.txt") as f:
    key = f.read()
genai.configure(api_key=key)

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
chat = model.start_chat(history=[])

def get_response(question):
    response = chat.send_message(question, stream=True)  # Enable streaming
    return response  # Return the response object

# Set the basic things over the page
st.set_page_config(page_title="Conversational AI Tutor")
st.title("AI Chatbot")

# Initial assistant message
st.chat_message("assistant").write("Hi, How may I help you?")

# Initialize session state for chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display the previous conversation history only if there are messages
if st.session_state["messages"]:
    for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).write(msg["content"])

# Taking user input (trigger on Enter)
user_input = st.chat_input("Type your message here...")

# When the user submits a message
if user_input:
    # Save user input in session state
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Generate assistant response
    response = get_response(user_input)  # Get the response object for streaming

    # Create a placeholder for displaying the response
    response_placeholder = st.empty()

    # Initialize a variable to store the entire response
    full_response = ""

    # Iterate over streamed response chunks
    for chunk in response:
        # Assuming `chunk` is an instance of Candidate
        # Retrieve the text from the first candidate part
        text_part = chunk.candidates[0].content.parts[0].text
        
        # Append the current part to the full response
        full_response += text_part + " "
        
        # Display the updated response in the placeholder
        response_placeholder.write(full_response.strip())  # Display line by line

    # Save the final response to session state
    st.session_state["messages"].append({"role": "assistant", "content": full_response.strip()})
