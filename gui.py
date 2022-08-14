from tkinter import *
from tkinter import filedialog

from csvparser import parse_csv
from pstparser import parse_pst_file
from app import compare_tickets_messages, create_csv_file


def getPst_FilePath():
    filePath = filedialog.askopenfile(filetypes=[("Outllok Data Files", ".pst")])
    if hasattr(filePath, 'name'):
        name = filePath.name
        name = name.replace('/', '\\')
        print(name)
        pst_input.insert(0, name)

def getCsv_FilePath():
    filePath = filedialog.askopenfile(filetypes=[("Comma Separated Values ", ".csv")])
    if hasattr(filePath, 'name'):
        name = filePath.name
        name = name.replace('/', '\\')
        print(name)
        csv_input.insert(0, name)

def openFile():
    pst_filePath = pst_input.get()
    csv_filePath = csv_input.get()
    if pst_filePath != '' and csv_filePath != '':
        tickets = parse_csv(csv_filePath)
        messages = parse_pst_file(pst_filePath)
        matches = compare_tickets_messages(tickets, messages)
        create_csv_file(matches)





window = Tk()
window.config(background='#eee')
window.geometry('420x420')
window.title('PST - CSV Parser')
# icon = PhotoImage( file='logo.png')
# window.iconphoto(False)

title = Label(
    window, 
    text='PST - CSV Parser', 
    font=('Arial', 16, 'bold'), 
    fg='black')
title.pack(pady=10)

pst_title = Label(window, text='Select PST file:', font=('Arial', 14, 'bold'))
pst_title.pack()

pst_input = Entry(window, font=('Arial', 14))
pst_input.pack()

open_pst_button = Button(window, text="Open pst", font=('Arial', 14), command=getPst_FilePath)
open_pst_button.pack(pady=10)

csv_title = Label(window, text='Select CSV file:',  font=('Arial', 14, 'bold'))
csv_title.pack(pady=20)

csv_input = Entry(window, font=('Arial', 14))
csv_input.pack()


open_csv_button = Button(window, text="Open csv", font=('Arial', 14), command=getCsv_FilePath)
open_csv_button.pack(pady=10)

ok_button = Button(window, text='OK', font=('Arial', 14), command=openFile)
ok_button.pack()

quit_button = Button(window, text='Quit', font=('Arial', 14), command=window.destroy)
quit_button.pack(pady=20, anchor='s')


window.mainloop()