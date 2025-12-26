from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from processing import preprocess_text

# 1 Mark – Keyword overlap
def evaluate_1m(model, student):
    model_words = set(preprocess_text(model).split())
    student_words = set(preprocess_text(student).split())

    if not model_words:
        return 0
    return len(model_words & student_words) / len(model_words)

# 3M & 10M – Semantic similarity
def evaluate_descriptive(model, student):
    model = preprocess_text(model)
    student = preprocess_text(student)

    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([model, student])
    score = cosine_similarity(tfidf[0], tfidf[1])[0][0]
    return score
