# NEED TO IMPLEMENT THE TWO SCRIPTS
from csvparser import parse_csv_file
from pstparser import parse_pst_file

messages = parse_pst_file(file_name='test.pst', filter='DUSWUSERSUPPSN1-')

for message in messages:
    print(message.date_time)