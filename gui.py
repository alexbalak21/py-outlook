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
        pst_input.delete(0, END)
        pst_input.insert(0, name)

def getCsv_FilePath():
    filePath = filedialog.askopenfile(filetypes=[("Comma Separated Values ", ".csv")])
    if hasattr(filePath, 'name'):
        name = filePath.name
        name = name.replace('/', '\\')
        csv_input.delete(0, END)
        csv_input.insert(0, name)

def openFile():
    pst_filePath = pst_input.get()
    csv_filePath = csv_input.get()
    if pst_filePath != '' and csv_filePath != '':
        tickets = parse_csv(csv_filePath)
        try:
            messages = parse_pst_file(pst_filePath)
        except:
            write_text_out('Error Opening PST')
            return
        try:
            matches = compare_tickets_messages(tickets, messages)
        except:
            write_text_out('Error Opening CSV')
            return
        if len(messages) < 1:
            write_text_out('0 Messages Trouvées')
            return
        if len(tickets) < 1:
            write_text_out('0 Tickets Trouvées')
            return
        create_csv_file(matches)
        nbr = len(matches)
        text_out.config(state=NORMAL)
        line = 'Nombre de correspondances trouvées: '+ str(nbr) +'\n'
        text_out.insert(END, line)
        for match in matches:
            line = match['name'] + ' - ' + str(match['delta']) + '\n'
            text_out.insert(END, line)
        text_out.config(state=DISABLED)
    else:
        text_out.config(state=NORMAL)
        text_out.insert(END, "NO PST or CSV selected\n")
        text_out.config(state=DISABLED)

def write_text_out(text:str):
    text_out.config(state=NORMAL)
    line = text + '\n'
    text_out.insert(END, line)
    text_out.config(state=DISABLED)







window = Tk()
window.config(background='#eee')
# window.geometry('420x420')
window.title('PST - CSV Parser')
# icon = PhotoImage( file='logo.png')
# window.iconphoto(False)

title = Label(
    window, 
    text='PST - CSV Parser', 
    font=('Arial', 16, 'bold'), 
    fg='black')
title.pack(pady=10)

pst_title = Label(window, text='Select PST file:', font=('Arial', 14))
pst_title.pack()

pst_input = Entry(window, font=('Arial', 14), width=28)
pst_input.pack()

open_pst_button = Button(window, text="Open pst", font=('Arial', 14), command=getPst_FilePath)
open_pst_button.pack(pady=(0,10))

csv_title = Label(window, text='Select CSV file:',  font=('Arial', 14))
csv_title.pack(pady=(20, 0))

csv_input = Entry(window, font=('Arial', 14), width=28)
csv_input.pack()


open_csv_button = Button(window, text="Open csv", font=('Arial', 14), command=getCsv_FilePath)
open_csv_button.pack(pady=(0,20))

frame = Frame(window)
frame.pack()

ok_button = Button(frame, text='OK', font=('Arial', 14), command=openFile)
ok_button.pack(side=LEFT, padx=(10,100))

quit_button = Button(frame, text='Quit', font=('Arial', 14), command=window.destroy)
quit_button.pack(side=RIGHT, padx=(100,10))


text_out = Text(window, height=12, width=50)
text_out.config(state=DISABLED)
text_out.pack(padx=10, pady=10)


window.mainloop()