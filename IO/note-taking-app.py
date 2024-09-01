def ask_user(prompt_message): 
    return input(prompt_message)

def file_exists(filename): 
    try:
        open(filename)
    except FileNotFoundError:
        return False
    else:
        return True

def create_file(filename): 
    open(filename, 'w').close()

def read_from_file(filename): 
    with open(filename, 'r') as f:
        return f.readlines()

def write_to_file(filename, content): 
    with open(filename, 'w') as f: 
        f.write(content)

def append_to_file(filename, content): 
    with open(filename, 'a') as f: 
        f.write(content)
    
def truncate_file(filename, size): 
    with open(filename, 'a') as f: 
        f.truncate(size)

def capture_filename(prompt_message): 
    return ask_user(prompt_message).strip().lower()

def display_options(filename): 
    print(f'a) Show all notes from {filename}')
    print(f'b) Delete {filename} and start over')
    print(f'c) Append {filename} a new note')
    print(f'd) Replace existing note in {filename}')

def capture_note(prompt_message): 
    return ask_user(prompt_message).strip()

def pick_menu_choice(prompt_message): 
    return ask_user(prompt_message).strip().lower()

def add_note(filename, note): 
    append_to_file(filename, note)

def replace_note(filename, note, position): 
    file_content = read_from_file(filename)
    file_content[position] = note
    write_to_file(filename, ''.join(file_content))

def get_all_notes(filename): 
    return [ n.rstrip('\n') for n in read_from_file(filename) ]

def main(): 
    filename = capture_filename('File name: ')

    if file_exists(filename): 
        display_options(filename)
        option_selected = pick_menu_choice('Select an option from the menu: ')

        if option_selected == 'a': 
            for note in get_all_notes(filename): 
                print(note)
        elif option_selected == 'b':
            truncate_file(filename, 0)
        elif option_selected == 'c': 
            note = capture_note('What you have in mind?: ')
            add_note(filename, note + '\n')
        elif option_selected == 'd': 
            note = capture_note('What you have in mind?: ')
            note_index = ask_user('Replace note at index: ')
            replace_note(filename, note + '\n', int(note_index))
        else: 
            print(f'Your option {option_selected}) is invalid!')
    else: 
        note = capture_note('What you have in mind?: ')
        create_file(filename)
        add_note(filename, note + '\n')

main()
