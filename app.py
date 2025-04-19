from flask import Flask, render_template, request
from utils import search_french_sentences

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        user_query = request.form["query"]
        results = search_french_sentences(user_query, top_k=5)
        return render_template("index.html", query=user_query, results=results)

if __name__ == "__main__":
    app.run(debug=True)
