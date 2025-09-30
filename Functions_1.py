import numpy as np
from threading import Event
from PIL import ImageFont, Image

font = ImageFont.truetype('C:/Users/user/Desktop/thinkbox/thinkbox/faceCall_pj/lib/NanumBarunGothicLight.ttf', 15)
img = np.full((480,640,3), 0, np.int8)
img_pil = Image.fromarray(img.astype(np.uint8))

# thread state
event = Event()

# global variances
kortext = ""
Engtext = ""
recognized_text = ""
translated_text = "Initial Value"

import numpy as np
from PIL import ImageDraw


def camera():
    global event, kortext, Engtext, font
    kor_state = ""
    kor_state_prev = ""

    import cv2
    print('cam activated')
    # open cam
    cap = cv2.VideoCapture(1)
    while True:
        none, frame = cap.read()
        # Inversion
        frame = cv2.flip(frame, 1)
        # subtitle background
        cv2.rectangle(frame, (0, 430), (640, 480), (0, 0, 0), -1)
        # print korean subtitle
        cv2.putText(frame, "[KOR]:", (10, frame.shape[0] - 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        # print translated subtitle
        cv2.putText(frame, "[ENG]:", (10, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
        cv2.putText(frame, Engtext, (70, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
        # creat img
        draw = ImageDraw.Draw(img_pil)
        img = np.array(img_pil)
        if kor_state_prev != kor_state and kor_state != "":
            draw.rectangle([(70, frame.shape[0] - 42), (640, frame.shape[0] - 26)], fill=(0, 0, 0))
            kor_state_prev = kor_state
            draw.text((70, frame.shape[0] - 43), kortext, (255, 255, 255), font=font)
        # frame + img integrate
        frame = cv2.addWeighted(frame, 1, img, 1, 0)
        # show video + subtitle
        cv2.imshow('VideoCall', frame)
        kor_state = kortext = str(recognized_text)
        Engtext = str(translated_text)
        key = cv2.waitKey(1) & 0xFF == ord('q')

        # shut thread if event is set
        if event.is_set():
            break
    # close cam
    cap.release()
    cv2.destroyAllWindows()
    print("cam_thread closed")

def subtitle():
    print('subtitle activated')
    global event, kortext, recognized_text, translated_text
    import speech_recognition as sr
    # initialize
    recognizer = sr.Recognizer()
    # microphone connect
    microphone = sr.Microphone()
    # speech recognition and translation into subtitle
    with microphone as source:
        while True:
            print("Listening...")
            audio = recognizer.listen(source)
            try:
                # speech recognition
                recognized_text = recognizer.recognize_google(audio, language="ko-KR")
                if recognized_text == "종료":
                    event.set()
                    break
                print("You said:   ", recognized_text)
                # translation
                translated_text = PAPAGO_translator(recognized_text)
                print("In English: ", translated_text)
            except sr.UnknownValueError:
                print("Failed to understand radio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"ERROR: {e}")
            except KeyboardInterrupt:
                print("KeyboardInterrupt")
        print("translator_thread closed")

def PAPAGO_translator(message):
    import sys
    sys.path.append('C:/Users/user/Desktop/thinkbox/thinkbox/faceCall_pj/papago_keys.py')
    import papago_keys as my
    import urllib.request
    # import keys as my
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

###########################################################################

def thread_subtitle():
    import threading
    # create thread
    subtitle_thread = threading.Thread(target=subtitle)

    # start thread
    subtitle_thread.start()

    # wait thread
    subtitle_thread.join()
    print("All Thread Closed")


if __name__ == "__main__":
    thread_subtitle()
    print("System down")

def giveEngtext():
    return translated_text
def giveKortext():
    return recognized_text