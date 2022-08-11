import pypff



# path to your pst file
opst = pypff.open('test.pst')
root = opst.get_root_folder()

# WHILE SUB FOLDER IS NOT 0 : GET IN ALL SUBFOLDERS AND GET MAILS
# def getAllMessages(item):
#     messages = []
#     msgs = []
#     nbrSubFolders = item.get_number_of_sub_folders()
#     while (nbrSubFolders > 0):
#         for i in nbrSubFolders:
#             currentFolder = item.get_sub_folder(i)
#             nbrMsg = currentFolder.get_number_of_sub_messages()
#             if (nbrMsg > 0):
#                 for j in nbrMsg:
#                     msg = currentFolder.get_sub_message(j)
#                     messages.append(msg)
#             msgs = getAllMessages(currentFolder)
#             messages.extend(msgs)
#     return messages

# OPEN SUB FOLDER BY SUB FOLDER
def checkSubFolders(folder):
    messages = []
    messages.extend(getMessages(folder))
    nbrSubFolders = folder.get_number_of_sub_folders()
    if (nbrSubFolders > 0):
        messages.extend(checkAllSubs(folder, nbrSubFolders))
    return messages


def checkAllSubs(folder, nbrOfSub):
    messages = []
    for n in range(nbrOfSub):
        current = folder.get_sub_folder(n)
        messages.extend(checkSubFolders(current))
    return messages


#CHECK MESSAGES
def getMessages(folder):
    messages = []
    nbrMsg = folder.get_number_of_sub_messages()
    if (nbrMsg > 0):
        for n in range(nbrMsg):
            msg = folder.get_sub_message(n)
            messages.append(msg)
    return messages


def getSubject(messages):
    for msg in messages:
        subject = msg.get_subject()
        delivery_time = msg.get_delivery_time()
        print('DATE :', delivery_time, 'SUBJECT :', subject)
    print('NBR OF MESSAGES :', len(messages))
    return 0
        

msgs = checkSubFolders(root)
print(len(msgs))
getSubject(msgs)




# print(len(allMessages))

# creation_time = msg.get_creation_time()
# delivery_time = msg.get_delivery_time()
# subject = msg.get_subject()