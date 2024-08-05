my_unique_list = []
my_left_overs = []

def add_item(item): 
    if item_exists(item): 
         return False   
   
    my_unique_list.append(item)
    return True

def reject_item(item):  
    if not item_exists(item):
        return False
    
    my_left_overs.append(item)
    return True 

def item_exists(item):
    return item in my_unique_list

# add_item scenario
add_item(1)
add_item(2)
add_item(3)
add_item(1)
add_item(2)
add_item(3)

# reject_item scenario
print(my_unique_list)

reject_item(3)
reject_item(10)
reject_item(1)
reject_item(4)
reject_item(2)

print(my_left_overs)
