from cgitb import text
from logging import root
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox


root = tk.Tk()
root.title('...?')
root.geometry('600x600')
root.configure(background='#ffc8dd')


def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y -  button_1.winfo_y ()) < 40: 
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)

def accepted():
    messagebox.showinfo(
        '...................'
    )

def denied():
    button_1.destroy()
    

margin = Canvas(root, width=500, bg='#F7F8FB', height=80, bd=0, highlightthickness=0, relief='ridge')
margin.pack()
text.id = Label(root, bg='#F7F8FB', text='................................', fg='#590d20', font=('Mostserrat', 24, 'bold'))

text.id.pack()
button_1 = tk.Button(root, text='Não, .........', bg='#ffb3c1', command=denied, relief=RIDGE, bd=3, font=('Montserrat', 8, 'bold'))

button_1.pack()
root.bind('<Motion>', move_button_1)
button_2 = tk.Button(root, text='Sim, .......', bg='#ffb3c1', relief=RIDGE, bd=3, command=accepted, font=('Montserrat', 14, 'bold'))

button_2.pack()

root.mainloop()















