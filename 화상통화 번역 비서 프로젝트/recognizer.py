import speech_recognition as sr
import pyautogui

# 음성 인식기 초기화
recognizer = sr.Recognizer()

# 마이크 선택 (시스템에 연결된 마이크를 선택)
microphone = sr.Microphone()

# 자막을 표시할 화면 좌표 설정
x, y = 100, 100

# 자막 초기화
current_caption = ""

# 무한 루프로 음성 감지 및 자막 생성
with microphone as source:
    while True:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            # 음성을 텍스트로 변환 (한국어로 인식)
            recognized_text = recognizer.recognize_google(audio, language="ko-KR")
            print("You said:", recognized_text)

            # 자막 업데이트
            current_caption = recognized_text

            # 자막을 화면에 표시
            pyautogui.alert(current_caption, "Real-time Caption", timeout=1)
 
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

        except Exception as e:
            print(f"An error occurred: {e}")

            import keys2 as my
            project_id = "my.ClientID()"