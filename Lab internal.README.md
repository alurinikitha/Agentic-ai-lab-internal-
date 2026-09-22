# Image Retrieval / Visual QA System

## Overview

This project develops a multimodal system that retrieves the most relevant image for a user query and uses a vision-language model to answer questions about the retrieved image.

---

## Objective

To understand how multiple AI models can be combined in a pipeline for image retrieval and visual question answering.

---

## Pipeline

```text
User Question
↓
Image Embedding
↓
Image Retrieval
↓
Relevant Image
↓
Vision-Language Model
↓
Final Answer
```

---

## Technologies Used

* Python
* CLIP / OpenCLIP
* Google Gemini
* Pillow
* NumPy
* Git
* GitHub

---

## Project Structure

```text
image-visual-qa/
├── images/
├── embeddings.py
├── retrieve.py
├── visual_qa.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How It Works

The system converts images into embeddings and retrieves the image most relevant to the user's question. The retrieved image and question are then passed to a vision-language model to generate the final answer.

---

## Example

**Question:**

```text
How many students are visible?
```

**Output:**

```text
There are approximately 20 students visible.
```

---

## Learning Outcome

* Learned image embeddings and image retrieval.
* Learned multimodal AI pipelines.
* Learned Visual Question Answering.
* Learned how multiple AI models can work together.

---

## Future Improvements

* Add a Streamlit interface.
* Support more images.
* Improve image retrieval accuracy.
* Add image captions and search history.

---

## Author

**Nikitha Aluri**

