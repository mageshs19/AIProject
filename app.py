import streamlit as st
from openai import OpenAI, RateLimitError

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🤖 Simple AI Chat Agent")

user_input = st.text_input("You:")

if user_input:
    try:
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            st.write("**AI:**", response.choices[0].message.content)
    except RateLimitError:
        st.error("⚠️ Rate limit reached. Try again later or upgrade your OpenAI plan.")
