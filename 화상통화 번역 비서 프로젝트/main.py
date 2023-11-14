import threading 
import numpy as np
from PIL import ImageFont, ImageDraw, Image

font = ImageFont.truetype('C:/pythoncode/vscode/python/python_test_code/프로젝트/NanumGothicLight.ttf', 14)
img = np.full((480,640,3), 0, np.int8)
kortext = ""
img_pil = Image.fromarray(img.astype(np.uint8))

recognized_text = ""
translated_text = ""
subtitle = ""
subtitle2 = ""
def cam_thread():
    global kortext
    global subtitle
    global subtitle2
    import cv2
    print('cam activated')
    # open cam
    cap = cv2.VideoCapture(0)
    subtitle_state = ""
    while True:
        ret, frame = cap.read()
        # Inversion
        frame = cv2.flip(frame, 1)

        # subtitle background
        cv2.rectangle(frame, (0, 430), (640, 480), (0, 0, 0), -1)

        # print korean subtitle
        cv2.putText(frame, "[KOR]:", (10, frame.shape[0] - 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        draw = ImageDraw.Draw(img_pil)
        img = np.array(img_pil)
        draw.text((70, frame.shape[0] - 42), kortext, (255, 255, 255), font=font)
        # print translated subtitle
        cv2.putText(frame, "[ENG]:", (10, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
        cv2.putText(frame, subtitle2, (70, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

        # frame과 img source integrate
        frame = cv2.addWeighted(frame, 1, img, 1, 0)

        cv2.imshow('Communication_Assistant', frame)
        kortext = str(recognized_text)
        subtitle2 = str(translated_text)


        if subtitle_state != kortext:
            cv2.rectangle(img, (30, 430), (640, 440), (0, 0, 0), -1)
            frame = cv2.addWeighted(frame, 0, img, 1, 0)
            subtitle_state = kortext

        # 키보드 입력 받기
        key = cv2.waitKey(1) & 0xFF
        # 'q' to quit
        if key == ord('q'):
            break
        # different function(?)
        elif key == ord('t'):
            subtitle = "t"
        elif key == ord('y'):
            subtitle = "y"
    # close cam
    cap.release()
    cv2.destroyAllWindows()

def translation(message):
    import urllib.request
    import keys as my
    import json
    client_id = my.PAPAGO_ClientID()
    client_secret = my.PAPAGO_ClientSecret()
    encText = urllib.parse.quote(message)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        response_data = json.loads(response_body.decode('utf-8'))
        translated_text = response_data['message']['result']['translatedText']
        return translated_text
    else:
        print("Error Code:" + rescode)


def speech_translator():
    global recognized_text
    global translated_text
    import speech_recognition as sr
    # 음성 인식기 초기화
    recognizer = sr.Recognizer()
    # 마이크 선택 (시스템에 연결된 마이크를 선택)
    microphone = sr.Microphone()
    # 무한 루프로 음성 감지 및 자막 생성
    with microphone as source:
        while True:
            print("Listening...")
            audio = recognizer.listen(source)
            try:
                # 음성을 텍스트로 변환 (한국어로 인식)
                recognized_text = recognizer.recognize_google(audio, language="ko-KR")
                print("You said:   ", recognized_text)
                translated_text = translation(recognized_text)
                print("In English: ", translated_text)
            except sr.UnknownValueError:
                print("Failed to understand radio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"ERROR: {e}")



def speech_translator_thread():
    pass


if __name__ == "__main__":
    # 쓰레드 생성
    cam_thread = threading.Thread(target=cam_thread)
    speech_translator_thread = threading.Thread(target=speech_translator)

    # 쓰레드 시작
    cam_thread.start()
    speech_translator_thread.start()

    # 메인 쓰레드에서 쓰레드가 종료될 때까지 대기
    cam_thread.join()
    speech_translator_thread.join()