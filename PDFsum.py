import PyPDF2
from transformers import pipeline

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def summarize_text(text, max_length=150):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=max_length, min_length=30, do_sample=False)
    return summary[0]["summary_text"]

pdf_path = "path_to_your_file.pdf"
text = extract_text_from_pdf(pdf_path)
summary = summarize_text(text)
print("Summary:")
print(summary)
