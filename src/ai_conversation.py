# ai_conversation.py
import json
import os
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
    # Cross-platform absolute paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_en = os.path.join(BASE_DIR, "data", "data_en.json")
    data_bn = os.path.join(BASE_DIR, "data", "data_bn.json")
    model_en = os.path.join(BASE_DIR, "models", "conversation_model_en.joblib")
    model_bn = os.path.join(BASE_DIR, "models", "conversation_model_bn.joblib")

    train_model(data_en, model_en)
    train_model(data_bn, model_bn)

    # Load models
    vectorizer_en, model_en = load_model(model_en)
    vectorizer_bn, model_bn = load_model(model_bn)      

    vectorizer, model = joblib.load("models/conversation_model_en.joblib")
print(vectorizer.get_feature_names_out())  # see vocabulary
print(model.classes_)  

print(get_local_response("What is your name?", vectorizer_en, model_en))
print(get_local_response("তোমার নাম কি?", vectorizer_bn, model_bn))