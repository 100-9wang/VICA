from tkinter import *





VC_GUI = Tk()

VC_GUI.title("VICA Client: A")
VC_GUI.geometry("1000x600")
VC_GUI.configure(bg = "#ffffff")

def btn_clicked():
    print("Button Clicked")

canvas = Canvas(
    VC_GUI,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = "C:/Users/user/Desktop/tkinter_pr/Proxlight_Designer_Export/background.png")
background = canvas.create_image(
    553.0, 283.5,
    image=background_img)

btn_call_img = PhotoImage(file = "C:/Users/user/Desktop/tkinter_pr/Proxlight_Designer_Export/img0.png")
btn_call = Button(
    VC_GUI,
    image = btn_call_img,
    borderwidth = 0,
    highlightthickness = 0,
    width= 112,
    height=34,
    command = start_camera_stream,
    text = 'start Video Call',
    relief = "flat")
btn_call.pack(anchor =tk.CENTER, expand=True)

btn_call.place(
    x = 426, y = 332,
    width = 112,
    height = 34)

btn_finishCall_img = PhotoImage(file = "C:/Users/user/Desktop/tkinter_pr/Proxlight_Designer_Export/img1.png")
btn_finishCall = tk.Button(
    VC_GUI,
    image = btn_finishCall_img,
    borderwidth = 0,
    highlightthickness = 0,
    width= 112,
    height=34,
    command = stop_videoCall,
    text = 'Leave Video Call',
    relief = "flat")
btn_finishCall.pack(anchor =tk.CENTER, expand=True)

btn_finishCall.place(
    x = 426, y = 400,
    width = 112,
    height = 34)

label_ipInput_img = PhotoImage(file = "C:/Users/user/Desktop/tkinter_pr/Proxlight_Designer_Export/img_textBox0.png")
label_ipInput_bg = canvas.create_image(
    481.5, 194.5,
    image = label_ipInput_img)

box_ipInput = Entry(
    bd = 0,
    bg = "#f4f3f3",
    highlightthickness = 0)

box_ipInput = tk.Text(VC_GUI, width=251.0, height=31)
box_ipInput.pack()

box_ipInput.place(
    x = 356.0, y = 178,
    width = 251.0,
    height = 31)

label_subjectInput_img = PhotoImage(file = "C:/Users/user/Desktop/tkinter_pr/Proxlight_Designer_Export/img_textBox1.png")
label_subjectInput_bg = canvas.create_image(
    481.5, 277.5,
    image = label_subjectInput_img)

box_subjectInput = Entry(
    bd = 0,
    bg = "#f4f3f3",
    highlightthickness = 0)

box_subjectInput = tk.Text(VC_GUI, width=251.0, height=31)
box_subjectInput.pack()

box_subjectInput.place(
    x = 356.0, y = 261,
    width = 251.0,
    height = 31)

VC_GUI.resizable(False, False)
VC_GUI.mainloop()
