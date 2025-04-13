import streamlit as st
import openai

# Load API Key from Streamlit Secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("🤖 Simple AI Chat Agent")

user_input = st.text_input("You:")

if user_input:
    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        st.write("**AI:**", response['choices'][0]['message']['content'])
