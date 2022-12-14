from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from os.path import exists



from csvparser import parse_csv
from pstparser import parse_pst_file
from app import compare_tickets_messages, create_csv_file




def getPst_FilePath():
    filePath = filedialog.askopenfilename(filetypes=[("Outllok Data Files", ".pst")])
    if not filePath:
        return
    name = filePath.replace('/', '\\')
    pst_input.config(fg='black')
    pst_input.delete(0, END)
    pst_input.insert(0, name)

def getCsv_FilePath():
    filePath = filedialog.askopenfilename(filetypes=[("Comma Separated Values ", ".csv")])
    if not filePath:
        return
    name = filePath.replace('/', '\\')
    csv_input.config(fg='black')
    csv_input.delete(0, END)
    csv_input.insert(0, name)

selected_csv = False

def select_csv():
    file_path = filedialog.asksaveasfilename(defaultextension='.csv',filetypes=[("Comma Separated Values ", ".csv")])
    global selected_csv
    if not file_path:
        save_input.config(state=NORMAL)
        selected_csv = False
        return
    name = file_path.replace('/', '\\')
    save_input.delete(0, END)
    save_input.insert(0, name)
    selected_csv = True
    save_input.config(state=DISABLED)
    return

def save_csv():
    global matches
    file_name = ''
    file_path = save_input.get()
    if len(matches) < 1:
        write_text_out('No Data to Save.')
        return
    global selected_csv
    if selected_csv:
        try:
            file_name = create_csv_file(matches, result_csv_file=file_path)
            write_text_out('File created : ' + file_name)
            save_button.config(state=DISABLED)
            return
        except:
            write_text_out('Could not write csv file.')
            return
    if not file_path.endswith('.csv'):
        write_text_out('Seletc valid csv file.')
        return
    if exists(file_path):
        yes = messagebox.askyesno(title='Remplace', message='File Exists.\nRemplace it ?')
        if yes:
            try:
                file_name = create_csv_file(matches, result_csv_file=file_path)
                write_text_out('File created : '+ file_name)
                return
            except:
                write_text_out('Error saving CSV.')
                return
        else:
            write_text_out('Aborted by user.')
            return
    else:
        try:
            file_name = create_csv_file(matches, file_path)
            write_text_out('File saved at : '+ file_name)
        except:
            write_text_out('Error saving at location : ' + file_path)
            return


matches = []

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
    if not exists(pst_filePath):
        write_text_out('PST file not found.')
        return
    if not exists(csv_filePath):
        write_text_out('CSV file not found.')
        return
    try:
        tickets = parse_csv(csv_filePath)
    except Exception as e:
        write_text_out('Error opening CSV file:')
        write_text_out(str(e))
        return
    try:
        messages = parse_pst_file(pst_filePath)
    except Exception as e:
        write_text_out('Error Opening PST:')
        write_text_out(str(e))
        return
    try:
        global matches
        matches = compare_tickets_messages(tickets, messages)
    except:
        write_text_out('Error Comparing:')
        # write_text_out(str(e))
        return
    if len(messages) < 1:
        write_text_out('0 Messages Trouv??es')
        return
    if len(tickets) < 1:
        write_text_out('0 Tickets Trouv??es')
        return
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

Label(window, text='Select PST file:', font=('Arial', 14)).pack()

pst_input = Entry(window, font=('Arial', 14), width=28)
pst_input.insert(0, 'D:\\DEV\\py-outlook\\test.pst')
pst_input.pack()

open_pst_button = Button(window, text="Open pst", font=('Arial', 14), command=getPst_FilePath)
open_pst_button.pack(pady=(0,10))

Label(window, text='Select CSV file:',  font=('Arial', 14)).pack(pady=(20, 0))

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

frame_save = Frame(window, width=400, height=40)
frame_save.pack(pady=10)
frame_save.pack_propagate(0)

label_save = Label(frame_save, text='Save CSV:', font=('Arial', 14)).pack(side=LEFT)
save_input = Entry(frame_save, font=('Arial', 14))
save_input.pack(side=LEFT)
browse_button = Button(frame_save,font=('Arial', 14), text='Browse', command=select_csv)
browse_button.pack(padx=5)
save_button = Button(window, text='Save', font=('Arial', 14), command=save_csv)
save_button.pack(pady=10)

window.mainloop()