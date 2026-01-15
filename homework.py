from tkinter import *
from PIL import Image, ImageTk
import urllib.request
from io import BytesIO

root = Tk()
root.title("домашнє завдання")

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

def toggle_var2():
    if var2.get() == 1:
        var3.set(0)

def toggle_var3():
    if var3.get() == 1:
        var2.set(0)

url = "https://i.ibb.co/GftfCr9R/2026-01-12-153229.png"
data = urllib.request.urlopen(url).read()
img = Image.open(BytesIO(data))
img = img.resize((642, 75), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)

img_label = Label(root, image=photo)
img_label.image = photo
img_label.grid(row=1, column=0, padx=10, pady=10)

check_button1 = Checkbutton(root, text="Увiмкнути щось?", variable=var1)
check_button1.grid(row=1, column=1, sticky=W, padx=10)

check_button2 = Checkbutton(root, text="Поставити 2", variable=var2, command=toggle_var2)
check_button2.grid(row=3, column=1, sticky=W, padx=10)

check_button3 = Checkbutton(root, text="Поставити 12", variable=var3, command=toggle_var3)
check_button3.grid(row=4, column=1, sticky=W, padx=10)

root.mainloop()