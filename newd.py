from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
from tkinter import messagebox

root = Tk()
root.title("insta")
root.minsize(600, 500)
root.maxsize(600,  500)
HEIGHT = 500
WIDTH = 600
FONT = font.Font(family="Times New Roman", size="10", weight="bold")

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = Frame(root, bg='white')
frame.place(relwidth=1, relheight=1)

background_image = ImageTk.PhotoImage(Image.open(r"instalogo.png"))
background_label = Label(frame, image= background_image)
background_label.place(relx=-0.60, rely=0, relheight=1)

label1 = Label(frame, text="Download Instagram Reel", font= FONT, bd=5, fg="#0d1137", bg="white")
label1.place(relx=0.48, rely=0.1, relheight=0.1)

FONT = font.Font(family="Times New Roman", size="12", weight="bold")
label2 = Label(frame, text="Enter link address: ", font= FONT, bd=5, fg="#e52165", bg="white")
label2.place(relx=0.48, rely=0.25, relheight=0.1)

entry = Entry(frame, fg  = "#fbad50")
entry.place(relx=0.48, rely=0.35, relheight=0.05, relwidth=0.4)

button1 = Button(root, text="Download", font = FONT, bd=5, fg="black", bg="pink", activeforeground="pink", activebackground="red")
button1.place(relx=0.48, rely=0.42, relheight=0.06)

label2 = Label(frame, text="Instruction: ", font=FONT, bd=5, fg="black", bg="white")
label2.place(relx=0.48, rely=0.56, relheight=0.1)

FONT = font.Font(family="Times New Roman", size="10", weight="bold")
TEXT = "1. Only Public Account\n2. Enter the link address"

label2 = Label(frame, text=TEXT, font=FONT, bd=5, fg="#cd486b", justify=LEFT, bg="white")
label2.place(relx=0.48, rely=0.7, relheight=0.1)

root.mainloop()

