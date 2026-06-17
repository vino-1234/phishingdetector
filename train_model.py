import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv("dataset.csv")

X = data["text"]
y = data["label"]

vectorizer = TfidfVectorizer()

X_vector = vectorizer.fit_transform(X)

model = MultinomialNB()

model.fit(X_vector, y)

pickle.dump(model, open("phishing_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
import os

print("Model saved:", os.path.exists("phishing_model.pkl"))
print("Vectorizer saved:", os.path.exists("vectorizer.pkl"))
print("Model trained successfully")