# Huggingface Transformers를 사용하여 긴 글 요약

주어진 텍스트 파일의 내용을 Huggingface Transformers를 활용해 요약합니다.  
Python으로 구현된 간단하고 강력한 텍스트 요약 도구입니다.

---

## 주요 내용

### 수행 단계:
1. 입력 텍스트 파일을 불러옵니다.
2. Huggingface의 `pipeline`과 `facebook/bart-large-cnn` 모델을 사용합니다.
3. 지정된 길이 조건에 따라 간결한 요약문을 생성합니다.
4. 생성된 요약 결과를 터미널에 출력합니다.

---

### 가정:
1. 입력 텍스트는 `.txt` 형식의 일반 텍스트 파일입니다.
2. 사전 학습된 모델을 사용해 요약문을 생성합니다.
3. `facebook/bart-large-cnn` 모델은 뉴스와 같은 긴 글 형식의 텍스트에 적합합니다.

---

### 원문 예시 (example1.txt)
Climate change continues to have profound effects on the planet, causing rising sea levels, more frequent extreme weather events, and dramatic changes in ecosystems. Scientists around the world are working tirelessly to study these impacts and propose potential solutions to mitigate the worst effects of global warming. For instance, renewable energy sources like solar, wind, and hydroelectric power are being adopted at an unprecedented rate, but challenges in infrastructure and energy storage remain. Meanwhile, international agreements such as the Paris Accord aim to unite nations in a shared goal to limit global temperature rise to below 2 degrees Celsius. However, progress has been uneven, with some countries failing to meet their commitments. The urgency of addressing climate change cannot be overstated, as the decisions made today will shape the world for future generations.

### 요약 결과
Climate change is causing rising sea levels, extreme weather, and ecosystem changes. Scientists are studying impacts and proposing solutions, with renewable energy adoption increasing. However, infrastructure and storage challenges persist. The Paris Accord aims to limit global temperature rise, but progress has been uneven. Urgent action is needed to shape the future.

---

## 요구사항:
**다음 버전에서 테스트되었습니다**:
- **Python**: 3.8+
- **Transformers**: 4.33.2
- **PyTorch**: 2.0.1

필수 패키지 설치 방법:
```bash
pip install -r requirements.txt
