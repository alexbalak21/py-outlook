# NEED TO IMPLEMENT THE TWO SCRIPTS


def compare_tickets_messages(tickets, messages):
    matches = []
    for ticket in tickets:
        for message in messages:
            if ticket.key == message.key:
                if (ticket.number == message.number):
                    delta = ticket.date_time - message.date_time
                    name_time = {'name': ticket.name, 'delta': delta}
                    matches.append(name_time)
    return matches

def create_csv_file(tickets, result_csv_file='result.csv'):
    if len(tickets) == 0:
        raise ValueError('No tickets to store')
    csv = open(result_csv_file, 'w')
    for data in tickets:
        delta = str(data['delta']).replace(',',' ')
        line = data['name'] + ',' + delta + '\n'
        csv.writelines(line)
        file_name = csv.name
    csv.close()
    return str(file_name)