from transformers import pipeline

# Hugging Face의 감정 분석 Pipeline 생성
sentiment_analyzer = pipeline("sentiment-analysis")

# 분석할 텍스트
texts = [
    "I love using Hugging Face! It's amazing.",
    "This project is so challenging, I feel frustrated.",
    "Today is a good day. I'm feeling great!"
]

# 각 텍스트에 대해 감정 분석 수행
for text in texts:
    result = sentiment_analyzer(text)[0]
    print(f"Text: {text}")
    print(f"Sentiment: {result['label']}, Confidence: {result['score']:.2f}\n")
