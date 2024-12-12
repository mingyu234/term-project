# Sentiment Analysis using Hugging Face

## 소개
이 프로젝트는 Hugging Face의 `transformers` 라이브러리를 활용하여 텍스트 감정 분석을 수행합니다. `pipeline` 기능을 사용해 간단한 코드로 텍스트의 긍정적 또는 부정적인 감정을 분석할 수 있습니다.

## 주요 기능
- Hugging Face의 사전 학습된 모델을 사용하여 텍스트 감정을 분석합니다.
- 입력된 텍스트를 긍정(Positive) 또는 부정(Negative)으로 분류하고 신뢰도 점수를 제공합니다.

## 코드 설명
### 의존성
이 코드는 `transformers` 라이브러리를 필요로 합니다. 다음 명령어를 사용해 설치할 수 있습니다:

```bash
pip install transformers
```

### 코드 구조
```python
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
```

### 코드 설명
1. **라이브러리 임포트**: `transformers`의 `pipeline`을 가져옵니다.
2. **Pipeline 생성**: `pipeline("sentiment-analysis")`를 사용해 감정 분석 파이프라인 객체를 생성합니다.
3. **분석할 텍스트 정의**: 감정 분석을 수행할 문자열 리스트를 정의합니다.
4. **결과 출력**: 각 텍스트에 대해 감정 분석 결과와 신뢰도 점수를 출력합니다.

### 출력 예시
```plaintext
Text: I love using Hugging Face! It's amazing.
Sentiment: POSITIVE, Confidence: 0.99

Text: This project is so challenging, I feel frustrated.
Sentiment: NEGATIVE, Confidence: 0.96

Text: Today is a good day. I'm feeling great!
Sentiment: POSITIVE, Confidence: 0.98
```

## 활용 사례
- 소셜 미디어 게시글 감정 분석
- 리뷰 데이터의 긍정/부정 분류
- 사용자 피드백 분석

## 참고 자료
- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers)

## 라이선스
이 코드는 MIT 라이선스를 따릅니다.
