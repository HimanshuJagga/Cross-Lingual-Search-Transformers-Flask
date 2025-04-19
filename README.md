
# 🧠 Cross-Lingual Semantic Search (Transformers + Flask)

An end-to-end NLP project that allows users to search French sentences using English queries. Built with Hugging Face Transformers, Sentence Transformers, and deployed via Flask. This project showcases multilingual semantic search and real-world AI deployment.

---

## 🔍 Project Overview

This project simulates a multilingual semantic search engine:
- 🌍 Users enter **English queries**
- 🤔 The app uses **transformer-based embeddings** to understand meaning
- 🔍 It finds the **most similar French sentences**
- 🚀 Results are served via a web interface using **Flask**

This is ideal for demonstrating your skills in:
- Semantic search
- NLP
- Hugging Face Transformers
- Deployment with Flask

---

## 🎮 Demo Use Case

> "When he asked who had broken the window, all the boys put on an air of innocence." → "Lorsqu'il a demandé qui avait cassé la fenêtre, tous les garçons ont pris un air innocent."

> "The password is "Muiriel" → "Le mot de passe est « Muiriel"

Sample queries for better results are listed in `examples.txt`

---

## 📁 Folder Structure

```
Cross-Lingual-Search-Transformers-Flask/
├── app.py                         # Flask backend
├── utils.py                       # Loads model + performs search
├── embeddings.pkl                 # Stored embeddings and sentence pairs
├── Multilingual-Search-using-Transformers.ipynb  # Full notebook
├── examples.txt                   # Sample English queries
├── templates/
│   └── index.html                # UI form and results view
```

---

## 🚀 How to Run (Locally)

1. Clone this repo:
```bash
git clone https://github.com/HimanshuJagga/Cross-Lingual-Search-Transformers-Flask.git
cd Cross-Lingual-Search-Transformers-Flask
```

2. Install dependencies:
```bash
pip install flask sentence-transformers torch
```

3. Run the app:
```bash
python app.py
```

5. Open browser:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🚀 Technology Stack

- Python
- Hugging Face Transformers
- Sentence-Transformers
- PyTorch
- Flask
- HTML 

---

## 💡 Key Features

- Multilingual semantic search (English → French)
- Sentence embeddings with `MiniLM` multilingual model
- Cosine similarity for ranking
- Interactive UI with Flask
- Query examples via `examples.txt`

---

## 📊 Performance
- Top-1 Accuracy (~56.5%): This means the model retrieves the correct French sentence as the top result for about 56.5% of English queries.
- Zero-shot learning: The model was not trained or fine-tuned on this specific dataset — it is using its pre-trained knowledge to understand and match across languages.
- How to improve? You can improve this score by:
  - Fine-tuning on a larger or domain-specific dataset
  - Expanding the dataset with more aligned sentence pairs
  - Trying other models like LaBSE or XLM-R for higher multilingual performance

---

## 💬 Contact

Made with ❤️ by **Himanshu Jagga**
- GitHub: [https://github.com/HimanshuJagga](https://github.com/HimanshuJagga)
- LinkedIn: [https://www.linkedin.com/in/himanshu-jagga-b08ab6170/](https://www.linkedin.com/in/himanshu-jagga-b08ab6170/)
- Email: himanshujagga97@gmail.com
