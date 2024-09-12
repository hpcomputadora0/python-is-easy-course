def main(): 
    print(guess_my_lucky_number('number_1', 7))
    print(guess_my_lucky_number('number_7', 10))
    print(guess_my_lucky_number('number_5', 23))
    print(guess_my_lucky_number('number_5', 37))

def guess_my_lucky_number(key, value): 
    lucky_numbers = {
        'number_1': 7,
        'number_2': 13,
        'number_3': 23,
        'number_4': 29,
        'number_5': 37,
        'number_6': 42
    }

    try: 
        my_lucky_number = lucky_numbers[key]
    except KeyError: 
        return False
    else:
        return my_lucky_number == value
    
main()

