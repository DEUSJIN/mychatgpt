import streamlit as st
from utils import initialize, chat

st.title("My ChatGPT")

with st.sidebar:
    api_key = st.text_input("API_KEY", type="password")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "ai", "content": "Hello, i'm your AI assistant, what can i do for you?"}]
    if api_key not in st.session_state or st.session_state.api_key != api_key:
        st.session_state["api_key"] = api_key
    st.markdown("[GET API_KEY](https://openai.com)")

chat_input = st.chat_input()

for message in st.session_state["messages"]:
    print(str(message)+"===")
    st.chat_message(message["role"]).write(message["content"])

if chat_input and not api_key:
    st.info("Please input API_KEY")
    st.stop()
if chat_input and api_key:
    st.session_state["messages"].append({"role": "human", "content": chat_input})
    st.chat_message("human").write(chat_input)
    if "memory" not in st.session_state:
        st.session_state["memory"] = initialize(st.session_state["api_key"])
    with st.spinner("running..."):
        response = chat(chat_input, st.session_state.api_key, st.session_state["memory"])
    st.session_state["messages"].append({"role": "ai", "content": response})
    st.chat_message("ai").write(response)
