import streamlit as st
import genai_backend as demo

st.title("The More you know, the more you grow!!!")

if 'memory' not in st.session_state:
    st.session_state.memory=demo.demo_memory()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history=[]

for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.markdown(message['text'])
        
input_text=st.chat_input("Enter your Query here")
if input_text:
    with st.chat_message("user"):
        st.markdown(input_text)
    st.session_state.chat_history.append({"role":"user","text":input_text})
    chat_reply=demo.demo_conversation(input_text, memory =st.session_state.memory) 

    with st.chat_message("assistant"):
        st.markdown(chat_reply)
    st.session_state.chat_history.append({"role":"assistant","text":chat_reply})







