def collect_participants_data(total_participants): 
    participants_info = []

    for _ in range(total_participants): 
        participant_name = input('Enter your name: ')
        participant_country = input('Enter your country: ')
        participant_age = input('Enter your age: ')

        participants_info.append((participant_name, participant_country, participant_age))

    return participants_info

def save_participants_data(participants): 
    participants_file = open('participants-registred.txt', 'w')

    for participant in participants:
        name, country, age = participant

        participants_file.write(name + ' ') 
        participants_file.write(country + ' ') 
        participants_file.write(str(age) + '\n') 
    
    participants_file.close()

def get_all_participants_data(): 
    participants_file = open('participants-registred.txt', 'r')
    participants = []

    for participant in participants_file: 
        name, country, age = participant.rstrip('\n').split(' ')
        participants.append((name, country, int(age)))

    return participants

print(get_all_participants_data())
