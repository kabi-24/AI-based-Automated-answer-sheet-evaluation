import re

def parse_answers(text):
    """
    Extracts question number, marks, and answer text
    Format:
    Q1 (1M) Answer: ...
    Q2 (3M) Answer: ...
    """
    pattern = r"(Q\d+)\s*\((\d+)M\).*?Answer:\s*(.*?)(?=Q\d+\s*\(|$)"
    matches = re.findall(pattern, text, re.DOTALL)

    data = []
    for qno, marks, ans in matches:
        data.append({
            "question": qno,
            "marks": int(marks),
            "answer": ans.strip()
        })
    return data
