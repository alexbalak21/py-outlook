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


tickets = []
with open('jira.csv', 'r') as csv_file:
    render = csv.reader(csv_file)
    for row in render:
        row = row[0]
        row = row.split(';')
        if(row[0] == ''):
            break
        if (row[1] == 'ID de ticket'):
            continue
        ticket_name = row[0]
        ticket_date_time = row[2]
        current_ticket = Ticket(key=ticket_name, InputDate_time=ticket_date_time)
        tickets.append(current_ticket)

ticket = tickets[96]
print('TICKET NUMBER', ticket.number)
print('HOUR : ',ticket.date_time.hour)
print('MINUTE : ',ticket.date_time.minute)
