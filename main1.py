import tkinter 
import PIL.Image, PIL.ImageTk
import cv2
from functools import partial
import threading
import time
import imutils

SET_WIDTH = 1000
SET_HEIGHT = 500

stream = cv2.VideoCapture("Run-out.mp4")


def play(speed):
    print("speed = {}".format(speed))
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
    grabbed, frame = stream.read()
    print(grabbed)
    frame = imutils.resize(frame, width=SET_WIDTH,height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

 

def pending(decision):
    #Display Pending Image
    frame = cv2.cvtColor(cv2.imread('pending.jpg'), cv2.COLOR_BGR2RGB)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image = frame, anchor = tkinter.NW)

    #wait for 1 second
    time.sleep(3)

    #Display Decision
    frame = cv2.cvtColor(cv2.imread(decision + '.jpg'), cv2.COLOR_BGR2RGB)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image = frame, anchor = tkinter.NW)

def out():
    thread = threading.Thread(target = pending, args = ("out",))
    thread.daemon = 1
    thread.start()
    print("PLayer is Out")

def not_out():
    thread = threading.Thread(target = pending, args = ("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is Not Out")




window = tkinter.Tk()
window.title('Third Umpire Decision Review System')
cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"),cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width = SET_WIDTH, height = SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0,anchor = tkinter.NW, image = photo)
canvas.pack()

#buttons to control playback
btn = tkinter.Button(window,text = "<< BACK (FAST)",width =50,command=partial(play,-25))
btn.pack()

btn = tkinter.Button(window,text = "<< BACK-(SLOW)",width =50,command=partial(play,-2))
btn.pack()

btn = tkinter.Button(window,text = " FORWARD-(FAST) >>",width =50,command=partial(play,25))
btn.pack()

btn = tkinter.Button(window,text = " FORWARD-(SLOW) >>",width =50,command=partial(play,2))
btn.pack()

btn = tkinter.Button(window,text = "GIVE OUT",width =50,command= out)
btn.pack()

btn = tkinter.Button(window,text = "GIVE NOT OUT",width =50,command=not_out)
btn.pack()

window.mainloop()