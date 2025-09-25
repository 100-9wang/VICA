# 화상통화 번역 비서 (VICA)

2인 프로젝트 

**한 줄 소개**

화상회의 및 통화내용을 실시간 번역하고 자막으로 표시하며, AI활용 회의 내용 요약 문서화 기능까지 제공하는 프로그램

---

## 프로젝트 기간 및 역할

- **기간:** 2023/10/01 ~ 2023/10/29
- **역할:**
    - 음성 인식/번역 모듈 구현
    - 영상 자막 표시 및 멀티스레딩 처리
    - GPT 기반 요약 모듈 API 연동 및 개발
    

---

## 사용 기술 스택

- **언어/프레임워크:** Python 3.10
- **API/서비스:** Naver Papago API, Google Translation API, OpenAI GPT-3.5 Turbo
- **기타:** 멀티스레딩(threading)

---

## 주요 기능 목표

1. **실시간 음성 인식**
    - 한국어 음성 → 텍스트 변환
    - 오류 처리 및 예외 대응
2. **실시간 번역**
    - Papago NMT 및 Google Cloud Translation API 연동
    - 한국어 → 영어 번역 (다국어 확장 가능)
3. **영상 자막 표시**
    - OpenCV + PIL을 활용한 자막 합성
    - 한글/영어 동시 표시
    - 지연 시간 1초 미만
4. **AI 내용 문서화 기능**
    - 번역된 텍스트 요약
    - 메시지 로그 저장 → trim() 메소드 사용 대화내용 정렬
    - doxc파일로 저장
5. **멀티스레딩 처리**
    - 음성 인식과 영상 처리 병렬 수행
    

---

## 트러블슈팅

- **음성 인식 실패**
    
    문제 :  `speech_recognition`라이브러리 사용 시, 음성이 제대로 인식되지 않음(`UnknownValueError`)
    
    원인 : 실제 화상통화 환경에서 잡음이 많아 음성 인식이 안정적으로 동작하지 않음
    
    해결 방안 : 
    
    - 마이크 장치 선택 (`microphone = sr.Microphone()`)
    - 소음 제거를 위한 코드 적용 (`recognizer.adjust_for_ambient_noise(source)`)
    - 예외 처리 (`try-except`)로 인식 실패 시 오류 메시지 출력 및 재시도
    
    성과 : 인식률 약 85% 이상 상승, 시스템 중단 없이 계속 음성 처리 가능
    
- **번역 API 실패**
    
    문제 : Papago API 호출 시 인증 정보 오류 또는 `HTTP 401` 발생
    
    원인 : 메소드 호출 인증 path 오류 
    
    해결 방안 : 
    
    - 코드에서 `keys.py`를 사용해 Client ID/Secret 가져오기 (`client_id = my.PAPAGO_ClientID()`)
    - `try-except`로 오류 발생 시 재시도 로직 구현
    
    성과 :  인증 오류 문제 해결, 번역 기능 안정화, keys.py로 키 분리로 인해 보안 강화
    
- **지연 문제**
    
    문제 : OpenCV 화면에 자막이 제대로 표시되지 않거나, 지연 발생
    
    원인 : 동기 처리 시 병목 현상 발생
    
    해결 방안 : 
    
    - `threading.Thread`으로 음성 인식, 번역, 영상 자막을 멀티스레드를 사용해 독립적으로 처리
    - PIL 라이브러리를 사용하여 한글 글꼴 적용 (`NanumGothicLight.ttf`)
    - OpenCV 프레임과 PIL 이미지 합성 (`cv2.addWeighted`)
    
    성과 : 영상 지연 0.5~1초 수준으로 단축, 한글/영문 자막 정상 표시
    
- **GPT 호출 지연**
    
    문제 : OpenAI GPT 호출 시 API 키 오류 또는 네트워크 문제로 응답 지연
    
    원인 : 공용 API를 사용하다보니 트래픽이 많이 몰리는 시간대에는 호출이 늦어지는 상황 발생
    
    해결 방안 : 최대한 오류를 줄이기 위해 예외처리 `try-except` 를 사용해 예외 처리 후 재시도하는 방식으로 진행
    
    성과 : 응답 시간 1~2초 상승, 오류 시 재작성을 통해 요약 내용 정상 출력 
    

---

## 결과물 & 시연

- 메인UI
<img width="619" height="501" alt="Image" src="https://github.com/user-attachments/assets/018be038-8134-451e-8175-c52d1fe5a194" />


- CNN Model 이미지 학습
<img width="1270" height="708" alt="Image" src="https://github.com/user-attachments/assets/9069118f-d49c-4b03-9780-25494db65b48" />


- 얼굴 인식1
<img width="929" height="494" alt="Image" src="https://github.com/user-attachments/assets/4251dade-2642-46ef-a34a-91058c4425e7" />


- 얼굴 인식2
<img width="920" height="548" alt="Image" src="https://github.com/user-attachments/assets/17200029-aff2-4147-bf7b-8884c22b5a61" />


- 문서 요약
<img width="632" height="580" alt="Image" src="https://github.com/user-attachments/assets/4ab16366-b162-4e3a-b4a5-3e49700e6250" />

[Notion] https://www.notion.so/2-2796a2e81c4e8120bd04c8f6ecbb5e72?source=copy_link

---

## 향후 개선 계획

- 자막 UI 개선 (투명 overlay, 위치/크기 조정)
- 다국어 번역 지원 확대
- 성능 최적화: 비동기 처리, 캐싱, 프레임 해상도 조절
