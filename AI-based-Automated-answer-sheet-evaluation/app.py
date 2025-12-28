import streamlit as st
import nltk
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from PyPDF2 import PdfReader
import docx
import pytesseract
from PIL import Image

# -------- TESSERACT PATH --------
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\shari\Downloads\tesseract-ocr-w64-setup-5.5.0.20241111.exe"

# -------- NLTK --------
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# -------- EXTRACT TEXT --------
def extract_text(file):
    name = file.name.lower()
    if name.endswith(".pdf"):
        reader = PdfReader(file)
        return " ".join([p.extract_text() or "" for p in reader.pages])
    elif name.endswith(".docx"):
        doc = docx.Document(file)
        return " ".join([p.text for p in doc.paragraphs])
    elif name.endswith((".png", ".jpg", ".jpeg")):
        img = Image.open(file)
        return pytesseract.image_to_string(img)
    else:
        return file.read().decode("utf-8")

# -------- PREPROCESS --------
def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if w.isalnum() and w not in stop_words]
    return " ".join(tokens)

# -------- PARSE ANSWERS --------
def parse_answers(text):
    pattern = r"(Q\d+)\s*\((\d+)M\).*?Answer:\s*(.*?)(?=Q\d+\s*\(|$)"
    matches = re.findall(pattern, text, re.DOTALL)
    data = []
    for qno, marks, ans in matches:
        data.append({"qno": qno, "marks": int(marks), "answer": ans.strip()})
    return data

# -------- 1M --------
def eval_1m(model, student):
    m = set(preprocess(model).split())
    s = set(preprocess(student).split())
    return len(m & s) / len(m) if m else 0

# -------- 3 & 10M --------
def eval_similarity(model, student):
    model, student = preprocess(model), preprocess(student)
    vec = TfidfVectorizer()
    tfidf = vec.fit_transform([model, student])
    return cosine_similarity(tfidf[0], tfidf[1])[0][0]

# -------- STREAMLIT PAGE CONFIG --------
st.set_page_config(page_title="AI Answer Sheet Evaluation", layout="wide")

# -------- GALAXY THEME CSS --------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap');

body {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    color: #ffffff;
}

/* Title */
.big-font {
    font-family: 'Orbitron', sans-serif;
    font-size: 60px !important;
    color: #00FFFF;
    text-align: center;
    margin-bottom: 5px;
    text-shadow: 2px 2px 8px #ff00ff;
}

/* Subtitle */
.sub-font {
    font-family: 'Orbitron', sans-serif;
    font-size: 22px;
    color: #ffffff;
    text-align: center;
    margin-top: 0px;
    margin-bottom: 40px;
}

/* Custom uploader header */
.custom-upload-header {
    font-family: 'Orbitron', sans-serif;
    font-size: 22px;
    color: #00FFFF;
    text-shadow: 2px 2px 6px #ff00ff;
    margin-bottom: 10px;
}

/* Uploader box */
div.stFileUploader > label > div {
    border: 2px solid #00FFFF !important;
    border-radius: 12px;
    padding: 10px;
    color: #00FFFF;
    font-weight: bold;
    background: rgba(255,255,255,0.05);
    transition: 0.3s;
}
div.stFileUploader > label > div:hover {
    border-color: #ff00ff !important;
    color: #ff00ff;
    box-shadow: 0 0 15px #ff00ff;
}

/* Button */
div.stButton > button {
    background: linear-gradient(90deg, #ff00ff, #00ffff);
    color: #000000;
    font-size: 18px;
    padding: 12px 28px;
    border-radius: 15px;
    font-weight: bold;
}

/* DataFrame table */
.dataframe tbody tr:nth-child(even) {
    background-color: #1b1b2f;
}
.dataframe thead th {
    background-color: #ff00ff;
    color: #ffffff;
    text-align: center;
}

/* Progress bar */
.stProgress > div > div > div > div {
    background-color: #00ffff;
}
</style>
""", unsafe_allow_html=True)

# -------- HEADER --------
st.markdown('<h1 class="big-font">🌌 AI Answer Sheet Evaluation</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-font">Evaluate typed and handwritten answer sheets automatically </p>', unsafe_allow_html=True)

# -------- FILE UPLOADERS --------
st.markdown('<div class="custom-upload-header">🧑‍🏫 Upload Model Answer Sheet</div>', unsafe_allow_html=True)
model_file = st.file_uploader(
    "Choose Model Answer Sheet (PDF / DOCX / TXT / IMAGE)",
    type=["pdf", "docx", "txt", "png", "jpg", "jpeg"]
)

st.markdown('<div class="custom-upload-header">🧑‍🎓 Upload Student Answer Sheet</div>', unsafe_allow_html=True)
student_file = st.file_uploader(
    "Choose Student Answer Sheet (PDF / DOCX / TXT / IMAGE)",
    type=["pdf", "docx", "txt", "png", "jpg", "jpeg"]
)

# -------- EVALUATE BUTTON --------
if st.button("Evaluate Complete Question Paper"):
    if not model_file or not student_file:
        st.error("Please upload both model and student answer sheets.")
    else:
        model_text = extract_text(model_file)
        student_text = extract_text(student_file)

        model_data = parse_answers(model_text)
        student_data = parse_answers(student_text)

        results = []
        total = 0
        obtained = 0

        for m, s in zip(model_data, student_data):
            max_m = m["marks"]
            total += max_m
            if max_m == 1:
                score = eval_1m(m["answer"], s["answer"])
            else:
                score = eval_similarity(m["answer"], s["answer"])
            marks = round(score * max_m, 2)
            obtained += marks
            results.append([m["qno"], max_m, round(score, 2), marks])

        df = pd.DataFrame(
            results,
            columns=["Question", "Max Marks", "Similarity", "Marks Obtained"]
        )

        st.success("✅ Evaluation Completed Successfully")
        st.dataframe(df, use_container_width=True)
        st.markdown(f"## 🧮 Total Score: **{obtained} / {total}**")
        st.progress(obtained / total)
