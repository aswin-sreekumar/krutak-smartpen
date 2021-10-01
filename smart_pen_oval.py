from tkinter import *
import pyautogui
from PIL import Image, ImageGrab
import easyocr

originx = 0
originy = 0

thickness = 1
fileName = 'test'
window = Tk()
window.title("")
window.geometry(str(pyautogui.size().width-100) +"x"+str(pyautogui.size().height-100))

canvas = Canvas(window, width=pyautogui.size().width-100, height=pyautogui.size().height-100, bg='white')


def paint(event):
    # get x1, y1, x2, y2 co-ordinates
    x1, y1 = (event.x-thickness), (event.y-thickness)
    x2, y2 = (event.x+thickness), (event.y+thickness)
    canvas.create_oval(x1, y1, x2, y2, fill='black', outline='black')
    origin_set(event)



def clear(event):
    canvas.delete("all")


def origin_set(event):
    global originx
    global originy
    originx, originy = event.x, event.y


def ML(event):
    x = window.winfo_rootx()+canvas.winfo_x()
    y = window.winfo_rooty()+canvas.winfo_y()
    x1 = x+canvas.winfo_width()*2
    y1 = y+canvas.winfo_height()*2
    # x1 = x+pyautogui.size().width-100
    # y1 = y+pyautogui.size().height-100
    ImageGrab.grab().crop((x, y, x1, y1)).save("res.png")
    # add codes for ML text detection

    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext('res.png')
    print(result[0][1])


canvas.bind('<B1-Motion>', paint)
canvas.bind("<Button-1>", origin_set)
# canvas.bind("<Button-3>", clear)
canvas.bind("<Double-Button-1>", ML)

canvas.pack()
window.mainloop()
