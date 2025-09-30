from vidstream import ScreenShareClient, StreamingServer, CameraClient
import tkinter as tk
import socket
import Functions_1 as my
import threading


def thread_subtitle():
    # create thread
    subtitle_thread = threading.Thread(target=my.subtitle)
    # start thread
    subtitle_thread.start()
    # wait thread
    subtitle_thread.join()
    print("Subtitle Closed")


# my current local ip address
def my_current_ip():
    print(f"my_ip_address: {my_ip_address}")


my_ip_address = socket.gethostbyname(socket.gethostname())
print(f"my_ip_address: {my_ip_address}")
server = StreamingServer(my_ip_address, 3000)

# button functions

# create server and start listening
def createAndListenToServer():
    server_thread = threading.Thread(target=server.start_server)
    server_thread.start()

# start sharing screen/camera to server in target ip
# warnings: port numbers must be different from self-server's
# warnings: port numbers must match to the target server's
def start_screen_sharing():
    screen_client = ScreenShareClient(box_ipInput.get(1.0, 'end-1c'), 5000)
    sendScreen_thread = threading.Thread(target=screen_client.start_stream)
    sendScreen_thread.start()
def start_camera_stream():
    camera_client = CameraClient(box_ipInput.get(1.0, 'end-1c'), 5000)
    sendCam_thread = threading.Thread(target=camera_client.start_stream)
    generateSubtitle_thread = threading.Thread(target=my.subtitle)
    sendCam_thread.start()
    generateSubtitle_thread.start()




# tkinter = GUI creating library
# GUI

window = tk.Tk()
window.title("VideoCall GUI")
window.geometry('519x494')


icon_path = "C:/Users/user/Desktop/thinkbox/thinkbox/faceCall_pj/lib/images.ico"
window.iconbitmap(icon_path)

# my_ip button
btn_ip = tk.Button(window, text="My ip address", width=50, command=my_current_ip)
btn_ip.pack(anchor=tk.CENTER)
result_label = tk.Label(window, text="")
result_label.pack()

# server button
btn_listen = tk.Button(window, text="Start Listening", width=50, command=createAndListenToServer)
btn_listen.pack(anchor=tk.CENTER, expand=True)

# ip input box
label_ipInput = tk.Label(window, text="target ip")
label_ipInput.pack()
box_ipInput = tk.Text(window, height=1)
box_ipInput.pack()

# sharing buttons
btn_streamScreen = tk.Button(window, text="Start Screen Sharing", width=50, command=start_screen_sharing)
btn_streamScreen.pack(anchor=tk.CENTER, expand=True)
btn_camera = tk.Button(window, text="Start Camera Stream", width=50, command=start_camera_stream)
btn_camera.pack(anchor =tk.CENTER, expand=True)


window.mainloop()