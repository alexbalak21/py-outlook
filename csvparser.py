import csv
from datetime import datetime

class Ticket:
    def __init__(self, key:str, InputDate_time:str) -> None:
        self.key = key
        name_number = key.split('-')
        self.name = name_number[0]
        self.number:int = int(name_number[1])
        dateTime = InputDate_time.split(' ')
        date = dateTime[0]
        time = dateTime[1]
        hourMinute = time.split(':')
        dayMounthYear = date.split('/')
        self.date_time = datetime(
            year=int(dayMounthYear[2]), 
            month=int(dayMounthYear[1]), 
            day= int(dayMounthYear[0]),
            hour=int(hourMinute[0]),
            minute=int(hourMinute[1])
            )



def parse_csv_file(csv_file:str):
    tickets = []
    with open(csv_file, 'r') as csv_file:
        render = csv.reader(csv_file)
        for row in render:
            row = row[0]
            row = row.split(';')
            if(row[0] == ''):
                break
            if (row[1] == 'ID de ticket'):
                continue
            current_ticket = Ticket(key=row[0], InputDate_time=row[2])
            tickets.append(current_ticket)
    return tickets


tickets = parse_csv_file('test.csv')

for ticket in tickets:
    print(ticket.date_time)