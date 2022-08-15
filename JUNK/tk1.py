from tkinter import *

# button = you click it, then it does stuff

count 

count = 0


def click():
    global count
    count+=1
    print(count)

window = Tk()
button = Button(window,
                text="click me!",
                command=click,
                font=("Arial",24),
                compound='bottom')
button.pack()

window.mainloop()