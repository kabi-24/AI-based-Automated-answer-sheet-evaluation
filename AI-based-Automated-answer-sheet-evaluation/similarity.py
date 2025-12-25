from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def evaluate_answer(model_answer, student_answer):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([model_answer, student_answer])

    similarity_score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return similarity_score

# Sample answers
model = "Machine learning is a subset of artificial intelligence"
student = "ML is part of AI"

score = evaluate_answer(model, student)
print("Similarity Score:", round(score, 2))