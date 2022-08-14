# NEED TO IMPLEMENT THE TWO SCRIPTS
from csvparser import parse_csv
from pstparser import parse_pst_file

messages = parse_pst_file(file_name='test.pst')
tickets = parse_csv('test.csv')
print('NUMEBR OF MESSAGES :', len(messages))
print('NUMEBR OF TICKETS :', len(tickets))


def compare_tickets_messages(tickets, messages):
    matches = []
    for ticket in tickets:
        for message in messages:
            if ticket.key == message.key:
                if (ticket.number == message.number):
                    differance = ticket.date_time - message.date_time
                    name_time = [ticket.name, differance]
                    matches.append(name_time)
    return matches


matches = compare_tickets_messages(tickets, messages)

i = 0
for match in matches:
    i+=1
    delta = match[1]
    name = match[0]
    print(i, name, '-', str(delta))
