import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import time
import imutils


stream = cv2.VideoCapture(r"C:\Users\Anurag Nikam\OneDrive\Desktop\videoRUN.mp4")
flag = True

def play(speed):
    global flag
    print(f"You Clicked On Play. Speed is {speed}")
    
    #play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
        

    grabbed, frame = stream.read()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    Canvas.image = frame
    Canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    if flag:
        Canvas.create_text(155,26, fill="red", font="times 29 bold", text="Decision Pending")
    flag = not flag
       


def pending(decision):
    #display decision pending image
    frame = cv2.cvtColor(cv2.imread(r"C:\Users\Anurag Nikam\OneDrive\Desktop\2019 wc.webp"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    Canvas.image = frame
    Canvas.create_image(0,0, image=frame, anchor=tkinter.NW)


    #wait for 1 sec
    time.sleep(1)


    #Display sponsor image
    frame = cv2.cvtColor(cv2.imread(r"C:\Users\Anurag Nikam\OneDrive\Desktop\sponsor.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    Canvas.image = frame
    Canvas.create_image(0,0, image=frame, anchor=tkinter.NW)


    #wait for 1 sec
    time.sleep(1.5)


    #Display out/notout image
    if decision == 'out':
        decisionImg = r"C:\Users\Anurag Nikam\OneDrive\Desktop\out.jpg"
    else:
        decisionImg = r"C:\Users\Anurag Nikam\OneDrive\Desktop\not.not.jpg"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    Canvas.image = frame
    Canvas.create_image(0,0, image=frame, anchor=tkinter.NW)



    
  

def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")


def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")


def on_enter(event, color):
    event.widget['background'] = color

def on_leave(event, color):
    event.widget['background'] = color


#width and height of our main screen
SET_WIDTH = 650
SET_HEIGHT = 368


#tkinter gui starts here
window = tkinter.Tk()
window.title("Third Umpire Decision Review System")
cv_img = cv2.cvtColor(cv2.imread(r"C:\Users\Anurag Nikam\OneDrive\Desktop\wankhede.jpg"), cv2.COLOR_BGR2RGB)
Canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_Canvas = Canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
Canvas.pack()
window.configure(bg='black')  





#buttons to control playback

frame1 = tkinter.Frame(window)
frame1.pack(pady=10)
btn = tkinter.Button(window, text="<< previous (fast)", width=50, command=partial(play, -20), bg="blue", fg="black")
btn.config(font=("Helvetica", 12), padx=10, pady=5)
btn.pack()
btn.bind("<Enter>", lambda event, color="white": on_enter(event, color))
btn.bind("<Leave>", lambda event, color="blue": on_leave(event, color))


frame1 = tkinter.Frame(window)
frame1.pack(pady=10)
btn = tkinter.Button(window, text="<< previous (slow)", width=50, command=partial(play, -2), bg="blue", fg="black")
btn.config(font=("Helvetica", 12), padx=10, pady=5)
btn.pack()
btn.bind("<Enter>", lambda event, color="white": on_enter(event, color))
btn.bind("<Leave>", lambda event, color="blue": on_leave(event, color))


frame1 = tkinter.Frame(window)
frame1.pack(pady=10)
btn = tkinter.Button(window, text=" Next (fast) >>", width=50, command=partial(play, 20), bg="grey", fg="black")
btn.config(font=("Helvetica", 12), padx=10, pady=5)
btn.pack()
btn.bind("<Enter>", lambda event, color="white": on_enter(event, color))
btn.bind("<Leave>", lambda event, color="grey": on_leave(event, color))


frame1 = tkinter.Frame(window)
frame1.pack(pady=10)
btn = tkinter.Button(window, text=" Next (slow) >>", width=50,command=partial(play, 2), bg="grey", fg="black")
btn.config(font=("Helvetica", 12), padx=10, pady=5)
btn.pack()
btn.bind("<Enter>", lambda event, color="white": on_enter(event, color))
btn.bind("<Leave>", lambda event, color="grey": on_leave(event, color))


frame1 = tkinter.Frame(window)
frame1.pack(pady=10)
btn = tkinter.Button(window, text=" Give Out", width=50, command=out, bg="red", fg="black")
btn.config(font=("Helvetica", 12), padx=10, pady=5)
btn.pack()
btn.bind("<Enter>", lambda event, color="white": on_enter(event, color))
btn.bind("<Leave>", lambda event, color="red": on_leave(event, color))


frame1 = tkinter.Frame(window)
frame1.pack(pady=10)
btn = tkinter.Button(window, text=" Give Not Out", width=50 ,command=not_out, bg="green", fg="black")
btn.config(font=("Helvetica", 12), padx=10, pady=5)
btn.pack()
btn.bind("<Enter>", lambda event, color="white": on_enter(event, color))
btn.bind("<Leave>", lambda event, color="green": on_leave(event, color))



window.mainloop()
