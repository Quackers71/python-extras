# f-Strings

x = 1
y = 2

print('x = ' + str(x) + ', y = ' + str(y))

print('x = {}, y = {}'.format(x, y))

# f-Strings - must have python 3.6... or newer

print(f'x = {x}, y = {y}')

my_string = f'x = {x}, y = {y}'
print(my_string)

a = 1
b = 2.12341234
c = '3.1234123412'

# {variable:width.precision{type}}
# use f for float, s for string &... d for integer
print(f'{a:10d}, {b:10.3f}, {c:15s}')

# to find out what the variable represents use:
print(c.__repr__()) # or just use: 
print(repr(c))
