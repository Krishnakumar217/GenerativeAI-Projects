import google.generativeai as genai
import streamlit as st

# Set page configuration to full width
st.set_page_config(page_title="Python code reviewer", page_icon="💻")

f = open(r"F:\Data Science\GenAI Stuffs\Projects\Python Code Reviewer\gemini_api_key.txt")
key = f.read()
client = genai.configure(api_key=key)
#st.snow()
st.title("💬:rainbow[Python Code Reviewer & Generator]")
#st.subheader("GenAi")

prompt = st.text_area("Enter your python code")
if st.button("Generate"):
    #st.balloons()
    model = genai.GenerativeModel(
        model_name="models/gemini-1.5-pro-latest",
        system_instruction = """You are an AI Python Code Reviewer. I will provide Python code, 
        and you will review it to fix bugs, improve efficiency, and suggest best practices. 
        Respond only with the corrected version of the code inside a unique code block
        along with the proper short and clear explanation.""")

    response = model.generate_content(prompt)
    st.write(response.text)