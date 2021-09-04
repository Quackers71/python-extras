def get_savings():
    global savings
    savings = input('Enter your savings balance (e.g. 3.99): ')
    return float(savings)

def get_income():
    global income
    income = input('Enter your monthly income (e.g. 1003.99): ')
    return float(income)

def calculate_income():
    global final_income
    final_income = float(income) - float(savings)
    return float(final_income)


def print_savings(savings_in):
    print(f'Great! You have ${savings_in:,.2f} in savings.')

def print_income(income_in):
    print(f'You make ${income_in:,.2f} each month!')

def print_final_income(final_income_in):
    print(f'So you are left with ${final_income_in:,.2f}')


def main():
    income = get_income()
    savings = get_savings()
    final_income = calculate_income()
    print_income(income)
    print_savings(savings)
    print_final_income(final_income)

if __name__ == '__main__':
    main()
