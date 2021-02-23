import os
import PIL
import numpy as np
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from keras.models import load_model


def predict():
    img_size = 28
    image.save("image.jpg")
    img = Image.open("image.jpg").resize((img_size, img_size))
    single_X = (255 - np.array(img)).reshape(1, img_size*img_size)
    predicted = str(np.argmax(model.predict(single_X)))
    prediction.config(text=f" {predicted} ")


def paint(event):
    x1, y1 = (event.x - 20), (event.y - 20)
    x2, y2 = (event.x + 20), (event.y + 20)
    canvas.create_oval(x1, y1, x2, y2, fill="black", width=20)
    draw.line([x1, y1, x2, y2], fill="black", width=20)


def clear():
    prediction.config(text="__")
    canvas.delete('all')
    draw.rectangle((0, 0, 400, 400), fill="#FFFFFF")


def save():
    filename = "images//img1.jpg"
    count = 1
    while os.path.isfile(filename):
        count += 1
        filename = "images//img" + str(count) + ".jpg"
    image.save(filename)
    clear()


if __name__ == '__main__':
    model = load_model(filepath='./digit_predict_model', compile=True)
    root = Tk()
    root.geometry('600x540')
    root.title('DRAWING DIGITS RECOGNIZERS USING AI')
    root.resizable(0, 0)

    defaultFont = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD)
    modelFont = tkFont.Font(family='Helvetica', size=70, weight=tkFont.BOLD)
    width = 400
    height = 400
    canvas = Canvas(root, width=width, height=height, bg='white')
    canvas.pack()

    image = PIL.Image.new("L", (width, height), color='white')
    draw = ImageDraw.Draw(image)

    canvas.bind("<B1-Motion>", paint)
    canvas.pack(expand=YES, fill=BOTH)

    btClear = Button(
        canvas, text="CLEAR", fg='white', bg='black', font=defaultFont, command=clear
    )
    btPredict = Button(
        canvas, text="PREDICT", fg='white', bg='black', font=defaultFont, command=predict
    )
    btSave = Button(
        canvas, text="SAVE", fg='white', bg='black', font=defaultFont, command=save
    )
    btExit = Button(
        canvas, text="EXIT", fg='white', bg='black', font=defaultFont, command=root.quit
    )
    btPredict.place(x=250, y=475)
    btClear.place(x=10, y=475)
    btSave.place(x=140, y=475)
    btExit.place(x=505, y=10)

    prediction = tk.Label(
        canvas, text="__", font=modelFont, fg='yellow', bg='black'
    )
    prediction.place(x=480, y=420)
    root.mainloop()