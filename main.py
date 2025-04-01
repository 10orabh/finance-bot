import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

# Load environment variables
load_dotenv()
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Set up Streamlit interface
st.title("Finance Expert Assistant 💰")
st.write("Ask me anything about finance!")

# Create input text area
user_input = st.text_area("Enter your question:", height=100)

# Create submit button
if st.button("Get Answer"):
    if user_input:
        with st.spinner("Thinking..."):
            text = f"You are finance expert your task is to provide an insightful to the following user query related to finance: {user_input} for any other query please respond with 'i do not know'"
            
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": text,
                    }
                ],
                model="deepseek-r1-distill-llama-70b",
            )
            
            # Display the response
            st.write("### Response:")
            st.write(chat_completion.choices[0].message.content)
    else:
        st.warning("Please enter a question!")