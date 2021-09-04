# Lists outputing with f-Strings

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f'x[9] = {x[9]}')
print(f'x[-1] = {x[-1]}')
print(f'x[0:10:2] = {x[0:10:2]}')
print(f'id(x) = {id(x)}')
print(f'x = {x}')

x[2] = -2
print('x[2] = -2')
print(f'x = {x}')
print(f'id(x) = {id(x)}')
print('\r')

def print_list(list_in):
    list_in[2] *= 2
    print(list_in)

y = [0, 1, 2, 3]
print(y)
print_list(y.copy())
print(y)
