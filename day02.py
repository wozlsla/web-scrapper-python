"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""
def is_on_list(a, b):
    if b in a:
        return True
    else:
        return False

def get_x(a, b):
    return a[b]

def add_x(a, b):
    a.append(b)

def remove_x(a, b):
    a.remove(b)
  
# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)


# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #

# days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# if  'Wed' in days:
#     print("Is Wed on 'days' list?", True)

# print("The forth item in 'days' is: ", days[3])

# days.append('Sat')
# print(days)

# print(days[1:])
