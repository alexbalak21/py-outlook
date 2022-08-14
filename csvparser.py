from datetime import datetime

class Ticket:
    def __init__(self, name:str, InputDate_time:str) -> None:
        self.name = name
        name_number = name.split('-')
        self.key = name_number[0]
        self.number = int(name_number[1])
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


def parse_csv(file_name, separator = ';'):
    file = open(file_name, 'r')
    delCol2 = False
    lines = file.readlines()
    line1 = lines[0].rstrip().split(separator)
    if line1[1] == 'ID de ticket':
        lines.pop(0)
        delCol2 = True
    if len(line1[1]) == 7:
        delCol2 = True
    file.close()
    tickets = []
    for line in lines:
        line = line.rstrip()
        ticket = line.split(separator)
        if delCol2:
            ticket.pop(1)
            ticketObj = Ticket(name=ticket[0], InputDate_time=ticket[1])
            tickets.append(ticketObj)
    return tickets
