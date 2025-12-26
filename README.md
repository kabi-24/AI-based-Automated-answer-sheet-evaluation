# AI-Based Automated Answer Sheet Evaluation System

## Project Overview
This project focuses on evaluating student answer sheets automatically using **Artificial Intelligence (AI)** and **Natural Language Processing (NLP)** techniques. The system analyzes students’ answers, compares them with model answers, and assigns marks based on semantic similarity, keyword matching, and relevance. This reduces manual effort and ensures faster and unbiased evaluation.

---

## Problem Statement
Manual evaluation of answer sheets is time-consuming, inconsistent, and prone to human bias. With an increasing number of students, traditional evaluation methods become inefficient. There is a need for an **automated answer evaluation system** that can accurately and fairly assess descriptive answers using AI techniques.

---

## Objectives
- Automatically evaluate descriptive answers  
- Compare student answers with model answers  
- Assign marks based on content similarity  
- Provide fast and unbiased evaluation  
- Reduce workload of teachers  
- Develop a simple web-based interface  

---

## Technologies Used
- **Python 3.9+**
- **Streamlit** (Web Interface)
- **NLTK** (Text Processing)
- **Scikit-learn** (TF-IDF & Similarity)
- **Pandas** (Data Management)

---

## Applications
- Schools and colleges  
- Online examinations  
- Practice tests and assessments  

---

## Conclusion

## Day 2 – Data Collection & Preprocessing

### Objective
To prepare textual data for automated answer evaluation using NLP techniques.

### Activities Performed
- Collected model answers and sample student answers
- Created dataset for evaluation
- Performed text preprocessing using NLP methods

### Preprocessing Steps
- Converted text to lowercase
- Removed punctuation and special characters
- Tokenized sentences into words
- Removed stopwords
- Cleaned and normalized text for feature extraction

### Outcome
Prepared clean textual data suitable for feature extraction and similarity computation.

## Day 3 – Feature Extraction & Similarity Measurement

### Objective
To evaluate student answers by measuring similarity with model answers using machine learning techniques.

### Activities Performed
- Implemented TF-IDF vectorization for text feature extraction
- Applied cosine similarity to compare model and student answers
- Generated similarity scores for descriptive answer evaluation

### Methodology
- Preprocessed text from Day 2 is converted into TF-IDF vectors
- Cosine similarity is calculated between model and student vectors
- Similarity score is used as the basis for mark allocation

### Outcome
Successfully measured semantic similarity between answers, forming the core evaluation logic of the system.

## Day 4 – Question-Wise Evaluation & Mark Allocation

### Objective
To implement automatic, question-wise answer evaluation and mark allocation.

### Work Done
- Parsed answers question-wise from model and student sheets
- Applied keyword matching for 1 mark questions
- Used TF-IDF and cosine similarity for 3 & 10 mark questions
- Automatically calculated question-wise and total marks

### Outcome
The system can now evaluate complete answer sheets fairly and generate structured results.
