# Agentic AI Lab Internal

**Name:** Nikitha Aluri
**Roll No:** 2311cs050078
**Batch:** IOT-ALPHA

---

# Prompt Chaining for Summarization

## Overview

This project demonstrates how prompt chaining can be used to improve the quality of text summarization. Instead of asking an AI model to directly summarize the text, the task is divided into multiple steps, where the output of one step becomes the input for the next step.

## Objective

The objective of this experiment is to understand how multi-step prompt pipelines can be used to extract important information, organize it, generate a summary, and review the final output.

## Prompt Chaining Pipeline

1. **Extract Information**

   * Identify the main topic, key points, benefits, challenges, and conclusion.

2. **Organize Information**

   * Arrange the extracted information into logical sections.
   * Remove duplicate information.

3. **Generate Summary**

   * Create a concise summary using the organized information.

4. **Review and Improve**

   * Check the summary for accuracy, missing information, repetition, grammar, and clarity.
   * Generate the final improved summary.

### Pipeline

```text
Original Text
      ↓
Step 1: Extract Important Information
      ↓
Step 2: Organize Information
      ↓
Step 3: Generate Summary
      ↓
Step 4: Review and Improve
      ↓
Final Summary
```

## Technologies Used

* Python
* OpenAI API
* Git
* GitHub
* Visual Studio Code

## Project Structure

```text
prompt-chaining-summarization/
│
├── summarize.py
├── input.txt
├── README.md
└── .gitignore
```

## How It Works

The program reads the text from `input.txt` and sends it through a sequence of prompts.

The output from Step 1 is passed to Step 2, the output from Step 2 is passed to Step 3, and the generated summary is passed to Step 4 for final review.

This demonstrates the concept of prompt chaining, where multiple AI tasks are connected together to complete a larger task.

## How to Run

### 1. Install the Required Python Package

```bash
pip install openai
```

### 2. Set Your OpenAI API Key

In the VS Code PowerShell terminal:

```powershell
$env:OPENAI_API_KEY="your-api-key"
```

Do not upload or share your API key publicly.

### 3. Run the Program

```bash
python summarize.py
```

The final improved summary will be displayed in the terminal.

## Example Input

The project uses a paragraph about the importance, benefits, and challenges of Artificial Intelligence in modern businesses.

## Learning Outcome

Through this experiment, I learned how to:

* Break a complex AI task into smaller steps.
* Connect multiple prompts into a pipeline.
* Pass the output of one AI task to another.
* Improve generated text through a review stage.
* Use the OpenAI API with Python.
* Manage a project using Git and GitHub.

## Future Improvements

* Save the output of each step into separate files.
* Add error handling for API failures.
* Allow users to provide their own text.
* Add a simple web interface.
* Compare single-prompt summarization with prompt chaining.

---

# SQL ReAct Agent with Tool Use

## Overview

This project demonstrates how a ReAct-based AI agent can interact with a database using database tools. The agent accepts questions in natural language, checks the database structure, generates SQL queries, executes them, and provides the answer.

## Objective

The objective of this experiment is to understand how AI agents can use external tools to interact with databases and answer questions using real database information.

## ReAct Agent Pipeline

1. **Understand Question**

   * Identify what information the user is asking for.

2. **Check Database**

   * List available tables.
   * Check the required table schema.

3. **Generate SQL**

   * Create a SQL `SELECT` query based on the user's question.

4. **Execute Query**

   * Execute the generated query using the database tool.
   * Observe the returned results.

5. **Generate Answer**

   * Use the query results to provide a simple natural-language answer.

### Pipeline

```text
User Question
      ↓
Understand Question
      ↓
List Tables
      ↓
Check Schema
      ↓
Generate SQL Query
      ↓
Execute SQL
      ↓
Observe Result
      ↓
Final Answer
```

## Technologies Used

* Python
* Google Gemini API
* LangChain
* LangGraph
* SQLite
* SQL
* Git
* GitHub
* Visual Studio Code

## Project Structure

```text
sql-react-agent/
│
├── agent.py
├── database.py
├── tools.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How It Works

The program uses a ReAct-style agent connected to database tools.

The agent can use the following tools:

* `list_tables` – Lists the available database tables.
* `get_schema` – Provides the structure of a selected table.
* `execute_sql` – Executes a read-only SQL `SELECT` query.

The agent decides which tools are needed to answer the user's question. The result from one tool can be used by the agent to decide the next action.

## How to Run

### 1. Install the Required Packages

```bash
pip install -r requirements.txt
```

### 2. Set Your Gemini API Key

Create a `.env` file in the project folder:

```env
GEMINI_API_KEY=your-gemini-api-key
```

Do not upload or share your API key publicly.

### 3. Create the Database

```bash
python database.py
```

### 4. Run the Agent

```bash
python agent.py
```

Then enter a question when prompted.

## Example Input

```text
How many employees are there?
```

Other example questions:

```text
Who has the highest salary?
```

```text
How many employees work in Engineering?
```

```text
What is the average salary of Engineering employees?
```

## Learning Outcome

Through this experiment, I learned how to:

* Build a ReAct-based AI agent.
* Connect an AI agent with database tools.
* Use natural language to query a database.
* Generate and execute SQL queries using an AI agent.
* Pass tool results back to the agent.
* Use Gemini with LangChain.
* Work with SQLite databases.
* Manage an AI project using Git and GitHub.

## Future Improvements

* Add a Streamlit web interface.
* Add MySQL or PostgreSQL support.
* Add more database tools.
* Add SQL query validation.
* Add error handling for SQL queries.
* Add data visualization.
* Add query history.

---

## Author

**Nikitha Aluri**
