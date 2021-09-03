


def get_name():
    print(f'In get_name: {dir()}')
    return input('Please enter your name: ')

def print_greeting(greeting_in):
    print(f'In print_greeting: {dir()}')
    print(greeting_in)
    print(f'This name shouldn\'t work {name}')

def get_greeting(name_in):
    print(f'In get_greeting: {dir()}')
    greeting_out = f'Hello {name_in}'
    return greeting_out

name = get_name()
greeting = get_greeting(name)
print_greeting(greeting)
#print(f'in tempy.py {dir()}')
