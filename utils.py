from llama_index import VectorStoreIndex, SimpleDirectoryReader, GPTListIndex
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')


def semantic_search(query):
    documents =SimpleDirectoryReader('data').load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return response


def summarize(file):
    documents = SimpleDirectoryReader('data').load_data()
    index = GPTListIndex.from_documents(documents)
    query_engine = index.as_query_engine(response_mode="tree_summarize")
    response = query_engine.query("Summarize the document")
    return response