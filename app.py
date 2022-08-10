import pypff
from datetime import date, datetime


# path to your pst file
opst = pypff.open('backup.pst')
root = opst.get_root_folder()

# WHILE SUB FOLDER IS NOT 0 : GET IN ALL SUBFOLDERS AND GET MAILS
def getAllMessages(item):
    messages = []
    msgs = []
    nbrSubFolders = item.get_number_of_sub_folders()
    while (nbrSubFolders > 0):
        for i in nbrSubFolders:
            currentFolder = item.get_sub_folder(i)
            nbrMsg = currentFolder.get_number_of_sub_messages()
            if (nbrMsg > 0):
                for j in nbrMsg:
                    msg = currentFolder.get_sub_message(j)
                    messages.append(msg)
            msgs = getAllMessages(currentFolder)
            messages.extend(msgs)
    return messages

# OPEM EACH SUB FOLDER
def checkSubFolders(folder):
    messages = []
    nbrSubFolders = folder.get_number_of_sub_folders()
    for n in nbrSubFolders:
        currentFolder = folder.get_sub_folder(n)
        messages.extend(getMessages(currentFolder))
    return messages

# OPEN SUB FOLDER UNTIL IT GOT NONE
def goToLastSubFolder(folder):
    messages = []
    messages.extend(getMessages(folder))
    gotSubFolder = True
    while goToLastSubFolder :
        if (folder.get_number_of_sub_folders() > 0):
            goToLastSubFolder = True
            folder = folder.get_sub_folder(0)
        else:
            goToLastSubFolder = False




#CHECK MESSAGES
def getMessages(folder):
    messages = []
    nbrMsg = folder.get_number_of_sub_messages()
    if (nbrMsg > 0):
        for j in nbrMsg:
            msg = folder.get_sub_message(j)
            messages.append(msg)
    else:
        return messages
    return messages

# print(len(allMessages))

# creation_time = msg.get_creation_time()
# delivery_time = msg.get_delivery_time()
# subject = msg.get_subject()