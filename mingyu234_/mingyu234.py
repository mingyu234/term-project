import cv2

def detect_faces(image_path, output_path="output.jpg"):
    # Haar Cascade XML 파일 로드
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # 이미지 로드
    image = cv2.imread(image_path)
    if image is None:
        print("이미지를 찾을 수 없습니다. 경로를 확인하세요.")
        return

    # 그레이스케일 변환 (성능 향상을 위해)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 얼굴 감지
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # 감지된 얼굴에 사각형 그리기
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # 결과 출력
    print(f"{len(faces)}개의 얼굴이 감지되었습니다.")
    cv2.imshow("Detected Faces", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 결과 저장
    cv2.imwrite(output_path, image)
    print(f"처리된 이미지가 {output_path}에 저장되었습니다.")

# 실행 예시
image_path = input("이미지 파일 경로를 입력하세요: ")
detect_faces(image_path)
