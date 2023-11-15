import socket
import cv2
import pickle
import struct

def start_client():
    # 소켓 생성 및 서버에 연결
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.0.3', 8888))

    # 웹캠 초기화
    cap = cv2.VideoCapture(1)

    try:
        while True:
            # 웹캠에서 프레임 캡처
            ret, frame = cap.read()
            data = pickle.dumps(frame)
            size = struct.pack('Q', len(data))  # 'L' 대신 'Q' 사용

            # 프레임 크기 전송
            client_socket.sendall(size)

            # 프레임 데이터 전송
            client_socket.sendall(data)

            # 키 입력 대기 시간 설정 (1밀리초)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        # 리소스 해제
        cap.release()
        client_socket.close()

if __name__ == "__main__":
    start_client()
