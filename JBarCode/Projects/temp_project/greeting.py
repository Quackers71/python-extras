def get_name():
    name = input('Please enter your name: ')
    return name

def print_greeting(greeting):
    print(greeting)

def get_greeting(name):
    greeting = f'Hello {name}'
    return greeting

def main():
    name = get_name()
    greeting = get_greeting(name)
    print_greeting(greeting)

if __name__ == "__main__":
    main()
