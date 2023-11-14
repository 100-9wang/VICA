import speech_recognition as sr
from google.cloud import translate
import keys2 as my

# 음성 인식기 초기화
recognizer = sr.Recognizer()

# 마이크 선택 (시스템에 연결된 마이크를 선택)
microphone = sr.Microphone()

# Google Cloud 프로젝트 ID (본인의 Google Cloud 프로젝트 ID로 설정)
project_id = "my.ClientID()"

# 번역 서비스 초기화
translate_client = translate.TranslationServiceClient()

with microphone as source:
    while True:
        try:
            print("Listening...")
            audio = recognizer.listen(source)

            # 음성을 텍스트로 변환 (한국어로 인식)
            recognized_text = recognizer.recognize_google(audio, language="ko-KR")
            print("You said:", recognized_text)

            # 번역 요청 생성
            response = translate_client.translate_text(
                parent=translate_client.location_path(project_id, "global"),
                contents=[recognized_text],
                target_language_code="en"  # 번역할 언어 코드 (영어)
            )

            # 번역 결과 출력
            translated_text = response.translations[0].translated_text
            print("Translated text:", translated_text)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
