import sys
from transformers import pipeline

def summarize_text(file_path):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python summarize_mine.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    summarized_text = summarize_text(file_path)
    print(f"Original Text:\n{open(file_path).read()}\n")
    print(f"Summarized Text:\n{summarized_text}")
