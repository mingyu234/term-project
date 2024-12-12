import re
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

# Huggingface 모델 로드 (한 번만 로드)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def clean_text(text):
    """
    텍스트 전처리 함수
    - 특수 문자 제거
    - 소문자 변환
    """
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text.lower()

def extract_keywords(text):
    """
    Huggingface 모델과 TF-IDF를 사용하여 키워드 추출
    """
    # 텍스트 전처리
    cleaned_text = clean_text(text)

    # Huggingface 요약 실행
    summary = summarizer(cleaned_text, max_length=50, min_length=5, do_sample=False)

    # 요약된 텍스트 추출
    summary_text = summary[0]['summary_text']

    # TF-IDF 기반 키워드 추출
    vectorizer = TfidfVectorizer(max_features=5, stop_words="english")
    X = vectorizer.fit_transform([summary_text])
    keywords = vectorizer.get_feature_names_out()

    return list(keywords)  # 리스트 형식으로 반환

def main():
    """
    프로그램 진입점
    """
    print("문맥에서 가장 중요한 단어를 추출하는 프로그램입니다.")
    file_path = input("분석할 텍스트 파일의 전체 경로를 입력하세요 (예: C:/path/to/file.txt): ")

    # 파일에서 텍스트 읽기
    try:
        with open(file_path, "r") as file:
            text = file.read()
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다. 올바른 경로를 입력하세요.")
        return
    except Exception as e:
        print(f"파일을 읽는 중 오류가 발생했습니다: {e}")
        return

    # 키워드 추출
    keywords = extract_keywords(text)
    print(f"\n추출된 주요 단어: {', '.join(keywords)}")

    # 결과 저장 옵션
    save_option = input("결과를 파일에 저장하시겠습니까? (y/n): ").strip().lower()
    if save_option == "y":
        with open("keywords_output.txt", "w") as output_file:
            output_file.write("Extracted Keywords:\n")
            output_file.write("\n".join(keywords))  # 키워드를 줄바꿈하여 저장
        print("결과가 'keywords_output.txt'에 저장되었습니다.")

if __name__ == "__main__":
    main()