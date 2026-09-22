Name : Nikitha Aluri 

Roll No: 2311cs050078 

IOT-ALPHA

# Prompt Chaining for Summarization

## Overview

This project demonstrates how prompt chaining can be used to improve the quality of text summarization. Instead of asking an AI model to directly summarize the text, the task is divided into multiple steps, where the output of one step becomes the input for the next step.

## Objective

The objective of this experiment is to understand how multi-step prompt pipelines can be used to extract important information, organize it, generate a summary, and review the final output.

## Prompt Chaining Pipeline

1. Extract Information

   * Identify the main topic, key points, benefits, challenges, and conclusion.

2. Organize Information

   * Arrange the extracted information into logical sections.
   * Remove duplicate information.

3. Generate Summary

   * Create a concise summary using the organized information.

4. Review and Improve

   * Check the summary for accuracy, missing information, repetition, grammar, and clarity.
   * Generate the final improved summary.

### Pipeline

text
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

### 1. Install the required Python package

```bash
pip install openai
```

### 2. Set your OpenAI API key

In the VS Code PowerShell terminal:

```powershell
$env:OPENAI_API_KEY="your-api-key"
```

Do not upload or share your API key publicly.

### 3. Run the program

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

## Author

Nikitha Aluri
