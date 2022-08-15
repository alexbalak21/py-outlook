from tkinter import *
from tkinter import filedialog

from csvparser import parse_csv
from pstparser import parse_pst_file
from app import compare_tickets_messages, create_csv_file


def getPst_FilePath():
    filePath = filedialog.askrun_compare(filetypes=[("Outllok Data Files", ".pst")])
    if hasattr(filePath, 'name'):
        name = filePath.name
        name = name.replace('/', '\\')
        pst_input.config(fg='black')
        pst_input.delete(0, END)
        pst_input.insert(0, name)

def getCsv_FilePath():
    filePath = filedialog.askrun_compare(filetypes=[("Comma Separated Values ", ".csv")])
    if hasattr(filePath, 'name'):
        name = filePath.name
        name = name.replace('/', '\\')
        csv_input.config(fg='black')
        csv_input.delete(0, END)
        csv_input.insert(0, name)

def run_compare():
    pst_filePath = pst_input.get()
    csv_filePath = csv_input.get()
    if not pst_filePath or not pst_filePath.endswith('.pst'):
        write_text_out('Select Correct PST file.')
        pst_input.config(fg='red')
        return
    if not csv_filePath or not csv_filePath.endswith('.csv'):
        write_text_out('Select Correct CSV file.')
        csv_input.config(fg='red')
        return
    try:
        tickets = parse_csv(csv_filePath)
    except Exception as e:
        write_text_out('Error opening CSV file:')
        write_text_out(str(e))
    try:
        messages = parse_pst_file(pst_filePath)
    except Exception as e:
        write_text_out('Error Opening PST:')
        write_text_out(str(e))
        return
    try:
        matches = compare_tickets_messages(tickets, messages)
    except:
        write_text_out('Error Comparing:')
        # write_text_out(str(e))
        return
    if len(messages) < 1:
        write_text_out('0 Messages Trouvées')
        return
    if len(tickets) < 1:
        write_text_out('0 Tickets Trouvées')
        return
        
    create_csv_file(matches)
    write_text_out('Number of matches found: '+ str(len(matches)))
    for match in matches:
        write_text_out(match['name'] + ' - ' + str(match['delta']))

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
pst_input.insert(0, 'D:\\DEV\\py-outlook\\test.pst')
pst_input.pack()

open_pst_button = Button(window, text="Open pst", font=('Arial', 14), command=getPst_FilePath)
open_pst_button.pack(pady=(0,10))

csv_title = Label(window, text='Select CSV file:',  font=('Arial', 14))
csv_title.pack(pady=(20, 0))

csv_input = Entry(window, font=('Arial', 14), width=28)
csv_input.insert(0, 'D:\\DEV\\py-outlook\\test.csv')
csv_input.pack()


open_csv_button = Button(window, text="Open csv", font=('Arial', 14), command=getCsv_FilePath)
open_csv_button.pack(pady=(0,20))

frame = Frame(window)
frame.pack()

ok_button = Button(frame, text='OK', font=('Arial', 14), command=run_compare)
ok_button.pack(side=LEFT, padx=(10,100))

quit_button = Button(frame, text='Quit', font=('Arial', 14), command=window.destroy)
quit_button.pack(side=RIGHT, padx=(100,10))


text_out = Text(window, height=12, width=50)
text_out.config(state=DISABLED)
text_out.pack(padx=10, pady=10)


window.mainloop()