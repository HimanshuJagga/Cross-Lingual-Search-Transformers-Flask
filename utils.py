import pickle
import torch
from sentence_transformers import SentenceTransformer, util

# Load model only once (multilingual)
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# Load saved embeddings and sentences
with open("embeddings.pkl", "rb") as f:
    data = pickle.load(f)

english_sentences = data["english_sentences"]
french_sentences = data["french_sentences"]
french_embeddings = data["french_embeddings"]

# Function to search top-k matching French sentences
def search_french_sentences(user_query, top_k=3):
    query_embedding = model.encode(user_query, convert_to_tensor=True)
    similarity_scores = util.cos_sim(query_embedding, french_embeddings)[0]
    top_k_scores = torch.topk(similarity_scores, k=top_k)

    results = []
    for score, idx in zip(top_k_scores[0], top_k_scores[1]):
        results.append({
            "french": french_sentences[idx],
            "score": round(score.item(), 4)
        })
    return results