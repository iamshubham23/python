from tkinter import *
from PIL import Image, ImageTk # type: ignore
window=Tk()
window.title("Password Manager")
img=Image.open("lockker.jpg")
logo_img=ImageTk.PhotoImage(img)
canvas=Canvas(window,height=200,width=200)
canvas.create_image(100,100,image=logo_img)
canvas.pack()
window.mainloop()