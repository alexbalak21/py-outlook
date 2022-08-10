import pypff
from datetime import date, datetime


# path to your pst file
opst = pypff.open('backup.pst')
root = opst.get_root_folder()

def getSubFolders(item, name):
    # subFoldersNbr = item.get_number_of_sub_folders()
    # nbrMsg = item.get_number_of_sub_messages()
    itemNbr = item.get_number_of_sub_items()
    # print(f"NBR SUB FOLDERS OF {name} : {subFoldersNbr}")
    print('--------------------------------')
    print(f"NBR SUB ITEMS OF {name} : {itemNbr}")
    print('--------------------------------')
    # print(f"NBR SUB MESSAGES OF {name} : {nbrMsg}")
    print('--------------------------------')
    return 0

# 3 subfolders, for me, only 2nd one has content
# Use 'root.get_number_of_sub_folders()' to see which folder is blan
rootSubItems = root.get_number_of_sub_items()
rootSubFolders = root.get_number_of_sub_folders()
rootSubMessages = root.get_number_of_sub_messages()
folder2 = root.get_sub_folder(1)
folder3 = folder2.get_sub_folder(1)
folder4 = folder3.get_sub_folder(0)
getSubFolders(folder4, 'INBOX')
msg = folder4.get_sub_message(0)
getSubFolders(msg, 'MSG')


creation_time = msg.get_creation_time()
delivery_time = msg.get_delivery_time()
subject = msg.get_subject()


print(delivery_time, subject)