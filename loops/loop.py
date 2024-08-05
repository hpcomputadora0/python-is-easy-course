# Helper functions
def is_prime(n): 
    if(n == 1):
        return False
    
    possible_factor = 1 
    number_of_factors = 0

    while(possible_factor <= n):
        if(i % possible_factor == 0): 
            number_of_factors += 1
        possible_factor += 1
        
    return True if number_of_factors <= 2 else False

def is_fizz_buzz(n): 
    return is_fizz(n) and is_buzz(n)

def is_buzz(n): 
    return n % 5 == 0

def is_fizz(n): 
    return n % 3 == 0

# Main entry.
for i in range(1, 101): 
    if(is_prime(i)): 
        print('Prime')
    elif(is_fizz_buzz(i)):
        print('FizzBuzz')
    elif(is_buzz(i)):
        print('Buzz')
    elif(is_fizz(i)):
        print('Fizz')
    else: 
        print(i)