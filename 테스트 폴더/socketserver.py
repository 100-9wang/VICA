import socket
import cv2
import pickle
import struct

def start_server():
    # 소켓 생성 및 바인딩
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.0.3', 8888))
    server_socket.listen(5)

    print("서버가 포트 8888에서 대기 중...")

    conn, addr = server_socket.accept()
    print(f"{addr}에서 연결됨")

    try:
        while True:
            # 소켓 연결 상태 확인
            data = conn.recv(8)
            if not data:
                print("연결이 종료되었습니다.")
                break

            # 수신된 프레임의 크기 확인
            size = struct.unpack('Q', data)[0]  # 'L' 대신 'Q' 사용
            data = b""
            while len(data) < size:
                packet = conn.recv(4096)
                if not packet:
                    break
                data += packet

            # 프레임 역직렬화 및 화면에 표시
            frame = pickle.loads(data)
            cv2.imshow('서버', frame)
            
            # 'q' 키를 누르면 루프 종료
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        # 연결 종료 및 창 닫기
        conn.close()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    start_server()
