# Removed unused import
import select
import streamlit as st
from pathlib import Path
from langchain_groq import ChatGroq
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
import sqlite3
from sqlalchemy import create_engine

st.set_page_config(layout="wide", page_icon=":computer:")
st.title("Chat with SQL DB")

LOCAL_DB_PATH = "Local_DB_Path"
MYSQL_DB_PATH = "USE_MYSQL_DB_PATH"

radio_opt = ["Use Local DB", "Use MySQL DB"]

selected_op = st.sidebar.radio("Select DB Type", radio_opt)

if radio_opt.index(selected_op) == 1:
    db_url = MYSQL_DB_PATH
    mysql_host = st.sidebar.text_input("Enter MySQL Host", type="default")  # Ensure this is correct
    mysql_user = st.sidebar.text_input("Enter MySQL User", type="default")
    mysql_password = st.sidebar.text_input("Enter MySQL Password", type="password")
    mysql_db = st.sidebar.text_input("Enter MySQL DB", type="default")
else:
    db_url = LOCAL_DB_PATH  # Ensure db_url is initialized

groq_api_key = st.sidebar.text_input("Enter Groq API Key", type="password")

llm = ChatGroq(api_key=groq_api_key, model_name="llama3-8b-8192", streaming=True)

if not db_url:
    st.error("Please enter MySQL DB URL")

if not groq_api_key:
    st.error("Please enter Groq API Key")

@st.cache_resource(ttl="2h")
def configure_db(db_url, host=None, user=None, password=None, db=None):
    if db_url == LOCAL_DB_PATH:
        db_filepath = (Path(__file__).parent / "my_database.db").absolute()
        engine = create_engine(f"sqlite:///{db_filepath}")
        return SQLDatabase(engine)
    elif db_url == MYSQL_DB_PATH:
        if not (mysql_host and mysql_user and mysql_password and mysql_db):
            st.error("Please enter MySQL Host, User, Password, and DB")
            st.stop()
        engine = create_engine(f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}")
        return SQLDatabase(engine)

if db_url == MYSQL_DB_PATH:
    db = configure_db(db_url, mysql_host, mysql_user, mysql_password, mysql_db)
else:
    db = configure_db(db_url)

# Toolkit
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

if "messages" not in st.session_state or st.sidebar.button("Clear Chat"):
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you with the database?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

user_query = st.chat_input(placeholder="Enter your query")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = agent.invoke({"input": user_query}, callbacks=[st_callback], handle_parsing_errors=True)
        st.session_state.messages.append({"role": "assistant", "content": response["output"]})
        st.markdown(response["output"])