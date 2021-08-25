#String slicing
name = 'The Pebble aka Quackers'
fullstr = name[:]
print(fullstr)

rev_ent_fullstr = name[::-1]
print(rev_ent_fullstr)

x = name[15:23]
print(x)

x_rev = name[-8:]
print(x_rev)

x_rev_then_rev = name[-8:][::-1]
print(x_rev_then_rev)

y = name[0]
print('The 1st character is ' + y)

z = name[-8]
print(z + ' is the best!')