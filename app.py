import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from Openai_agent import get_response
from func import execute_code

st.set_page_config(page_title="Data007🕵️", page_icon="🕵️", layout="wide")

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! How may I assist you today?"}
        ]

initialize_session_state()

st.title("Data007🕵️")
st.write("Data analysis and visualization made easy")

file, reset = st.columns([1, 1])
with file:
    uploaded_file = st.file_uploader("Choose a file", type=['csv'])

with reset:
    if st.button("Reset", type='primary', use_container_width=True):
        del st.session_state['messages']
        initialize_session_state()

if uploaded_file is not None:
    st.spinner("Analyzing the data...")
    st.write("File uploaded successfully")

    prompt = st.chat_input("Enter your question here")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    df = pd.read_csv(uploaded_file)

    if st.session_state.messages[-1]["role"] == "user":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_response(df, prompt)
                if response is not None:
                    output = execute_code(str(response['intermediate_steps'][0][0].tool_input['query']), df)
                    if isinstance(output, pd.DataFrame):
                        st.dataframe(output)
                    elif isinstance(output, plt.Figure):
                        st.pyplot(output)
                    else:
                        st.write(output) 
                    st.session_state.messages.append({"role": "assistant", "content": output})

