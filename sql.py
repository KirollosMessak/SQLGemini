from dotenv import load_dotenv
load_dotenv()

import sqlite3
import google.generativeai as genai
import os
import streamlit as st

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

#function to load gemini model and provide queries as response
def get_query (question, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro-002')
    response = model.generate_content([prompt[0], question])
    return response.text

#function to retrieve query from the databse
def read_sqlquery (sqlquery, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sqlquery)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return rows

#define prompt
prompt = [
    """You are an expert in converting English questions to SQL queries.
    
The SQL database is named STUDENT and has the following columns: NAME, CLASS, SECTION.

### Examples:

1️⃣ **Question:** How many entries of records are present?  
   **SQL Query:** SELECT COUNT(*) FROM STUDENT;

2️⃣ **Question:** Tell me all the students who study Data Science class.  
   **SQL Query:** SELECT NAME FROM STUDENT WHERE CLASS = 'DATA SCIENCE';

### Formatting Rules:
- **Do NOT include "```sql" or "```"** in your response.
- **Do NOT include "SQL" or any unnecessary text** in your response.
- **Only return the raw SQL query.**
"""
]


#Streamlit app
st.set_page_config(page_title='I can retrieve any sql query')
st.header('Gemini APP to retrieve SQL data')

question = st.text_input('INput', key='input')
submit = st.button('ask')

if submit:
    query = get_query(question, prompt)
    print(query)
    response = read_sqlquery(query, db='student.db')
    st.subheader('response is')
    for row in response:
        print(row)
        st.header(row)
