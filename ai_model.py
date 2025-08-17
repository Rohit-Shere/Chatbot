from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import START,END,StateGraph
from typing import Annotated,TypedDict
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import BaseMessage,HumanMessage
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import os

load_dotenv()
# st.session_state -> dict -> 
CONFIG = {'configurable': {'thread_id': 'thread-1'}}

llm = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash',
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2
)

class ChatState(TypedDict):
    message: Annotated[list[BaseMessage], add_messages]
    
    
def chat_node(state:ChatState):
    messages = state['message']
    response = llm.invoke(messages)
    return {"message": [response]}
    
graph= StateGraph(ChatState)



# adding the nodes
checkpointer = InMemorySaver()

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)

def chatbot_res(msg):
    res = chatbot.invoke({'messages': [HumanMessage(content=msg)]}, config=CONFIG)
    return res
# user_input=input("enter the query: ")


# for msg_chunk,metadata in chatbot.stream(
#     {'message': [HumanMessage(content=user_input)]},
#     config=CONFIG,
#     stream_mode='messages'
#     ):
#     if msg_chunk.content:
#         print(msg_chunk.content,end=" ",flush=True)
