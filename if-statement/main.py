def check_for_equality(a, b, c): 
    a = int(a)
    b = int(b)
    c = int(c)

    if a == b or a == c or b == c: 
        return True
    
    return False 

print(check_for_equality("5", 5, 1))
print(check_for_equality(1, "5", 5)) 
print(check_for_equality(5, 1, "5"))
print(check_for_equality(5, 5, "5"))
print(check_for_equality(1, "1", 5))
print(check_for_equality(1, "3", 5))
print(check_for_equality("3", "3", 5))