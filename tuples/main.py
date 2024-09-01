# Homework activity 1
song = {
    'name': 'Final Frontier',
    'genre': 'Electronic',
    'artist': 'Juno Reactor',
    'album': 'The Golden Sun of the Great East',
    'duration_in_seconds': 420,
    'number_of_likes': 1000000,
    'times_downloaded': 500000
}

for key, value in song.items(): 
    print(key, "-", value)

# Homework activity 2
def guessMyLuckyNumber(key, value): 
    lucky_lottery_numbers = {
        'number1': 7,
        'number2': 13,
        'number3': 23,
        'number4': 29,
        'number5': 37,
        'number6': 42
    }

    return True if (key in lucky_lottery_numbers and lucky_lottery_numbers[key] == value) else False 

print(guessMyLuckyNumber('number1', 7))
print(guessMyLuckyNumber('number7', 10))
print(guessMyLuckyNumber('number5', 23))
print(guessMyLuckyNumber('number5', 37))