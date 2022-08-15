from tkinter import *
from tkinter import filedialog

def click():
    global clickCounter
    clickCounter += 1
    print(clickCounter)
    counter.config(text=f"Counter: {clickCounter}")


def submit():
    username = entry.get()
    hello.config(text=f"Hello {username}")
    hello.pack()

def delete():
    entry.delete(0 ,END)

def openFile():
    filePath = filedialog.askopenfile()
    print(filePath)

window = Tk()
window.geometry('420x420')
window.title('PST CSV PARSER')
icon = PhotoImage( file='logo.png')
window.iconphoto(True, icon)

label = Label(
    window, 
    text='Hello World', 
    font=('Arial', 30, 'bold'), 
    fg='black')
    
label.pack()

clickCounter = 0

counter = Label(
    window,
    text=f"Counter: {clickCounter}"
)
counter.pack()

button = Button(window, text='Click Me', command=click)
button.pack()


hello = Label(window, text="", font=('Arial', 24, 'bold'))
hello.pack()

open_button = Button(window, text="Open", font=('Arial', 20, 'bold'), command=openFile)
open_button.pack()

entry = Entry(window, textvariable="Your Name", font=('Arial', 18))
entry.pack(side=LEFT)

submit_button = Button(window, text='Submit', font=('Arial', 14), command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="DELETE", font=('Arial', 14), command=delete)
delete_button.pack(side=RIGHT)


window.config(background='#eee')
window.mainloop()

