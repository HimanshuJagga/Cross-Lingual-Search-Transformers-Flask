🧠 Cross-Lingual Semantic Search (Transformers + Flask)

An end-to-end NLP project that allows users to search French sentences using English queries. Built with Hugging Face Transformers, Sentence Transformers, and deployed via Flask. This project showcases multilingual semantic search and real-world AI deployment.

🔍 Project Overview

This project simulates a multilingual semantic search engine:

🌍 Users enter English queries

🤔 The app uses transformer-based embeddings to understand meaning

🔍 It finds the most similar French sentences

🚀 Results are served via a web interface using Flask

This is ideal for demonstrating your skills in:

Semantic search

NLP

Hugging Face Transformers

Deployment with Flask

🎮 Demo Use Case

"What is your name?" → "Comment tu t'appelles ?"

"How are you?" → "Comment ça va ?"

Sample queries for better results are listed in examples.txt

📁 Folder Structure

Cross-Lingual-Search-Transformers-Flask/
├── app.py                         # Flask backend
├── utils.py                       # Loads model + performs search
├── embeddings.pkl                 # Stored embeddings and sentence pairs
├── Multilingual-Search-using-Transformers.ipynb  # Full notebook
├── examples.txt                   # Sample English queries
├── templates/
│   └── index.html                # UI form and results view

🚀 How to Run (Locally)

Clone this repo:

git clone https://github.com/yourusername/Cross-Lingual-Search-Transformers-Flask.git
cd Cross-Lingual-Search-Transformers-Flask

(Optional) Create a virtual environment:

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

Install dependencies:

pip install flask sentence-transformers torch

Run the app:

python app.py

Open browser:
http://127.0.0.1:5000

🚀 Technology Stack

Python

Hugging Face Transformers

Sentence-Transformers

PyTorch

Flask

HTML (Jinja templates)

💡 Key Features

Multilingual semantic search (English → French)

Sentence embeddings with MiniLM multilingual model

Cosine similarity for ranking

Interactive UI with Flask

Query examples via examples.txt

📊 Performance

Top-1 accuracy on test set: ~56.5% (zero-shot, 200 queries)

Can be improved with fine-tuning or dataset expansion

💬 Contact

Made with ❤️ by Himanshu Jagga

GitHub: https://github.com/HimanshuJagga

LinkedIn: https://www.linkedin.com/in/himanshu-jagga-b08ab6170/

Email: himanshujagga97@gmail.com
