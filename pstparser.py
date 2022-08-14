
import datetime
import pypff

class Message:
    def __init__(self, subject:str, key:str, number:int, date_time:datetime) -> None:
        self.subject = subject
        self.date_time = date_time
        self.key = key
        self.number = number


def parse_pst_file(file_name:str, filter= 'DUSWUSERSUPPSN1'):
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
def getMessages(folder, filter = 'DUSWUSERSUPPSN1'): 
    messages = []
    nbrMsg = folder.get_number_of_sub_messages()
    if (nbrMsg > 0):
        for n in range(nbrMsg):
            msg = folder.get_sub_message(n)
            subject = msg.get_subject()
            #FILTER SUBJECT BY filter 
            if filter in subject:
                delivery_time = msg.get_delivery_time()
                delivery_time = delivery_time.replace(microsecond=0)
                ticketNumber = get_ticket_number(subject, filter + '-')
                msgObj = Message(subject=subject, key=filter, number=ticketNumber, date_time=delivery_time)
                messages.append(msgObj)
    return messages


def get_ticket_number(subject:str, filter:str) -> int:
    pos = subject.index(filter) + len(filter)
    nbrStr = ''
    for i in range(4):
        nbrStr += subject[pos + i]
    return int(nbrStr)