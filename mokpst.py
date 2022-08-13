import inspect
import pypff


class Message:
    def __init__(self, subject:str, date_time:str) -> None:
        self.subject = subject
        self.date_time = date_time
        self.ticket_number = subject.split('-')[1]


def parse_pst_file(file_name:str, filter = ''):
    opst = pypff.open(file_name)
    root = opst.get_root_folder()
    messages = checkFolder(root, filter)
    return messages


def checkFolder(folder, filter:str):
    messages = []
    #CHECKS FOR MESSAGES
    messages.extend(getMessages(folder, filter))
    # CHECKS FOR SUBFOLDERS
    nbrSubFolders = folder.get_number_of_sub_folders()
    if (nbrSubFolders > 0): 
        messages.extend(parseAllSubFolders(folder=folder, filter=filter, nbrOfSub=nbrSubFolders))
    return messages


# PARSES ALL SUBFOLDERS AND CHECKS ALL SUBFOLDERS FOR MESSAGES AND SUBFOLDERS
def parseAllSubFolders(folder, filter, nbrOfSub):
    messages = []
    for n in range(nbrOfSub): #GET EACH SUBFOLDER AND CHECKS IT FOR MESSAGES AND SUBFOLDERS
        current = folder.get_sub_folder(n) #STORES CURRENT SUBFLODER
        messages.extend(checkFolder(current, filter)) #CHECKS FOR MESSAGES AND SUBFOLDERS, ADDS MESSAGES TO MESSAGES ARRAY IF ANY
    return messages


#CHECK MESSAGES AND RETURNS ALL MESSAGES OF FOLDER IN AN ARRAY
def getMessages(folder, filtrer = ''): 
    messages = []
    nbrMsg = folder.get_number_of_sub_messages()
    if (nbrMsg > 0):
        for n in range(nbrMsg):
            msg = folder.get_sub_message(n)
            modify_message(msg)
            subject = msg.get_subject()
            delivery_time = msg.get_delivery_time()
            message = [subject, msg.get_delivery_time()]
            messages.append(message)
    return messages


def modify_message(message):
    subject = message.get_subject()
    subject = 'DUSWUSERSUPPSN1-3451 ' + subject
    message.subject = subject
    print('SUBJECT = ', message.get_subject())




messages = parse_pst_file('test.pst', '')
