import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

from tools import list_tables, get_schema, execute_sql

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0
)

tools = [
    list_tables,
    get_schema,
    execute_sql
]

system_prompt = """
You are a SQL database assistant.

You answer questions using the available database tools.

Follow this process:

1. Identify what information is needed.
2. List the available tables when necessary.
3. Check the relevant table schema.
4. Write a SQL SELECT query.
5. Execute the query using the database tool.
6. Use the result to answer the user's question.

Only use SELECT queries.
Do not modify the database.

Give the final answer in simple English.
"""

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=system_prompt
)


def ask_database(question: str):
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        }
    )

    return result


if __name__ == "__main__":
    question = input("Ask a database question: ")

    result = ask_database(question)

    print("\nAgent Response:\n")
    print(result["messages"][-1].content)