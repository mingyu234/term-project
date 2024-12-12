# Keyword Extractor: 문맥에서 가장 중요한 단어를 추출하는 프로그램

## 프로젝트 개요
이 프로젝트는 Huggingface Transformers와 TF-IDF 알고리즘을 사용하여 주어진 텍스트에서 문맥적으로 중요한 단어를 추출하는 Python 기반의 오픈소스 프로그램입니다. 텍스트 파일을 입력으로 받아, 중요한 단어들을 추출하여 사용자에게 제공합니다.

---

## 주요 기능
1. **텍스트 전처리**:
   - 특수 문자 제거 및 소문자 변환.
2. **Huggingface 요약 모델 활용**:
   - 텍스트의 핵심 내용을 요약.
3. **TF-IDF 기반 키워드 추출**:
   - 요약된 텍스트에서 중요한 단어를 추출.
4. **결과 저장**:
   - 추출된 키워드를 텍스트 파일(`keywords_output.txt`)로 저장.

---

## 필수 설치 항목
프로그램 실행 전에 아래 모델과 패키지를 설치해야 합니다:

### **1. Python 버전**
- Python 3.8 이상.

### **2. Python 패키지**
다음 명령어로 필요한 라이브러리를 설치합니다:

- **transformers\==4.33.2**:
    - Huggingface Transformers 라이브러리로, 텍스트 요약에 사용됩니다.
- **torch**:
    - Huggingface 모델 실행을 위한 딥러닝 프레임워크.
- **scikit-learn**:
    - TF-IDF 알고리즘을 활용한 키워드 추출에 사용됩니다.

### **3. 자동 다운로드 모델**

코드 실행 중 `facebook/bart-large-cnn` 모델이 처음 실행 시 자동으로 다운로드됩니다.

- 모델 크기: 약 1.6GB.
- 저장 경로: `~/.cache/huggingface/transformers/`.

다운로드를 미리 수행하려면 아래 명령어를 사용할 수 있습니다:
```python
from transformers import pipeline
pipeline("summarization", model="facebook/bart-large-cnn")
```

## 실행 방법

1. **필수 라이브러리 설치**
    
    - 위 설치 항목을 따라 필요한 패키지를 설치합니다.
2. **프로그램 실행**
    
    - 프로그램 실행을 위해 아래 명령어를 입력합니다:
        
        `python keyword_extractor.py`
        
3. **텍스트 파일 입력**
    
    - 프로그램에서 요청하는 파일 경로에 텍스트 파일 경로를 입력합니다.
4. **결과 확인**
    
    - 추출된 주요 단어가 콘솔에 출력되며, 원하는 경우 결과가 파일로 저장됩니다.

## 실행 예제

1. 입력 파일 (summary_text.txt)
```
Open source projects provide a way for people to collaborate on software development, enabling innovation and community-driven growth.
```

2. 실행결과
```
추출된 주요 단어: open, source, projects, development, innovation
```

3. 저장된 파일 (keywords_output.txt)
```
Extracted Keywords:
open
source
projects
development
innovation
```

