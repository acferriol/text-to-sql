import re
from langchain_ollama.llms import OllamaLLM

db_url = "sqlite:///test.db"

template = """
You are a SQL generator. When given a schema and a user question, you must output only the SQL statement nothing else. No explanation is needed 

Schema: {schema}
User question: {query}
Output: (SQL only): 
"""

model = OllamaLLM(model="deepseek-r1:8b")


def extract_schema(db_url):
    pass


def to_sql_query(query, schema):
    pass


def clean_text(text):
    cleaned = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    return cleaned.strip()
