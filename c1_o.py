import openai
import streamlit as st

# Set OpenAI API key
openai.api_key = "sk-proj-3zEt8CmgVnvv73ROdtQLT3BlbkFJNHJxVpDCPFerlmQ5TLrF"

# Function to interact with GPT-3.5 chatbot
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# Streamlit app
def main():
    st.title("DKB Chatbot")

    with st.form("user_input_form"):
        user_input = st.text_input("You:")
        submitted = st.form_submit_button("Submit")

    if submitted:
        if user_input.lower() in ["quit", "exit", "bye"]:
            st.write("Goodbye!")
        else:
            response = chat_with_gpt(user_input)
            st.write("Chatbot:", response)

if __name__ == "__main__":
    main()
