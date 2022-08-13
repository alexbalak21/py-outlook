
import pypff


# path to your pst file
opst = pypff.open('testTwo.pst')
root = opst.get_root_folder()
        
class Message:
    def __init__(self, subject:str, date_time:str) -> None:
        self.subject = subject
        self.date_time = date_time
        self.ticket_number = subject.split('-')[1]



def checkFolder(folder):
    messages = []
    #CHECKS FOR MESSAGES
    messages.extend(getMessages(folder))
    # CHECKS FOR SUBFOLDERS
    nbrSubFolders = folder.get_number_of_sub_folders()
    if (nbrSubFolders > 0): 
        messages.extend(parseAllSubFolders(folder, nbrSubFolders))
    return messages


# PARSES ALL SUBFOLDERS AND CHECKS ALL SUBFOLDERS FOR MESSAGES AND SUBFOLDERS
def parseAllSubFolders(folder, nbrOfSub):
    messages = []
    for n in range(nbrOfSub): #GET EACH SUBFOLDER AND CHECKS IT FOR MESSAGES AND SUBFOLDERS
        current = folder.get_sub_folder(n) #STORES CURRENT SUBFLODER
        messages.extend(checkFolder(current)) #CHECKS FOR MESSAGES AND SUBFOLDERS, ADDS MESSAGES TO MESSAGES ARRAY IF ANY
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
                msgObj = Message(subject=subject, date_time=delivery_time)
                messages.append(msgObj)
    return messages


msgs = checkFolder(root)

for msg in msgs:
    print('SUBJECT :', msg.subject)
    print('DAY : ', msg.date_time.day)
    print('MOUNTH : ', msg.date_time.month)
    print('DAY : ', msg.date_time.year)
    print('HOUR :', msg.date_time.hour)
    print('MINUTES :', msg.date_time.minute)
