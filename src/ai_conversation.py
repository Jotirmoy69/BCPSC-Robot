# ai_conversation.py
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

def train_model(json_file, model_file):
    with open(json_file, encoding="utf-8") as f:
        data = json.load(f)

    questions = [item['question'] for item in data]
    answers = [item['answer'] for item in data]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(questions)
    model = MultinomialNB()
    model.fit(X, answers)

    joblib.dump((vectorizer, model), model_file)
    print(f"Model saved to {model_file}")

def load_model(model_file):
    vectorizer, model = joblib.load(model_file)
    return vectorizer, model

def get_local_response(query, vectorizer, model):
    X_test = vectorizer.transform([query])
    return model.predict(X_test)[0]

if __name__ == "__main__":
    train_model("../data/data_en.json", "../models/conversation_model_en.joblib")
    train_model("../data/data_bn.json", "../models/conversation_model_bn.joblib")
