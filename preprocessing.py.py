import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenization
    tokens = word_tokenize(text)

    # Stopword removal
    stop_words = set(stopwords.words('english'))
    cleaned_tokens = [word for word in tokens if word not in stop_words]

    return " ".join(cleaned_tokens)

# Sample data
model_answer = "Machine learning is a subset of artificial intelligence."
student_answer = "ML is part of AI."

print("Processed Model Answer:", preprocess_text(model_answer))
print("Processed Student Answer:", preprocess_text(student_answer))
