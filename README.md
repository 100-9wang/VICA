# 화상통화 번역 비서 (VICA)

> 실시간 화상 회의 및 통화에서 한국어 음성을 영어로 번역하여 자막을 표시하고, AI 기반으로 회의 내용을 요약·문서화하는 프로젝트

---

## 📅 프로젝트 개요
- **기간:** 2023.10.01 ~ 2023.10.29  
- **참여 인원:** 2인 프로젝트  
- **역할:**  
  - 음성 인식 / 번역 모듈 구현  
  - 영상 자막 표시 및 멀티스레딩 처리  
  - GPT 기반 요약 모듈 API 연동  

---

## 🛠 기술 스택
- **언어:** Python 3.10  
- **API:** Naver Papago API, Google Translation API, OpenAI GPT-3.5 Turbo  
- **라이브러리:** `speech_recognition`, `opencv-python`, `PIL`, `threading`  

---

## 🚀 주요 기능
1. **실시간 음성 인식**
   - `speech_recognition` 라이브러리 활용
   - 환경 소음 제거 및 예외 처리
2. **실시간 번역**
   - Papago 및 Google Translation API 연동
   - 한국어 → 영어 번역
3. **영상 자막 표시**
   - OpenCV + PIL 기반 자막 합성
   - 한글/영문 동시 출력
4. **회의 내용 요약**
   - OpenAI GPT-3.5 API 활용
   - 대화 로그를 요약해 문서화 (`.docx`)
5. **멀티스레딩**
   - 음성 인식, 번역, 자막 출력을 병렬 처리 → 지연 최소화

---

## 🔍 트러블슈팅
- **음성 인식 오류 (`UnknownValueError`)**
  - 원인: 환경 잡음  
  - 해결: `adjust_for_ambient_noise()` 적용 → 인식률 약 85% 확보
- **Papago API 인증 오류 (`HTTP 401`)**
  - 원인: 메소드 호출 인증 path 오류  
  - 해결: `keys.py` 분리 관리 + 재시도 로직 추가
- **자막 표시 지연**
  - 원인: 동기 호출로 병목 발생  
  - 해결: `threading` 적용 → 지연 0.5~1초 수준으로 단축
- **GPT 응답 지연**
  - 원인: 네트워크 트래픽  
  - 해결: `try-except` 예외 처리 및 재시도 → 안정적 요약 결과 확보

---

## 📷 실행 결과
https://www.notion.so/2-2756a2e81c4e805e9b0ef4d082a097f0?source=copy_link

---
