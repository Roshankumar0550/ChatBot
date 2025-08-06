import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain


def demo_chatbot():
    os.environ["GOOGLE_API_KEY"] = "AIzaSyBN-0EmF6dlcbXfpXTnSHOCS7TEdb5jFeg"
    demo_llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash-latest",
        temperature=0.0,
        max_tokens=500
    )
    return demo_llm

def demo_memory():
    llm_d=demo_chatbot()
    memory=ConversationBufferMemory(llm=llm_d)
    return memory

def demo_conversation(input_text,memory):
    llm_chain_data= demo_chatbot()
    llm_conversation=ConversationChain(
        llm=llm_chain_data,
        memory=memory,
        verbose=True)
    chat_reply=llm_conversation.predict(input=input_text)
    return chat_reply









