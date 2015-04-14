my_list = ['a', 'b', 'c']

print(my_list[2])

my_list.append('d')
print(my_list)

my_list.insert(2, 'e')
print(my_list)

my_list.extend(['a', 'f', 'g'])
print(my_list)

element = my_list.pop()
print(element)
print(my_list)

print(my_list.count('a'))

print(my_list.index('c'))

my_list.reverse()
print(my_list)

my_list.sort() # sorted(my_list) returns sorted rather than in place sort.
print(my_list)

my_list.remove('c')
print(my_list)

del my_list[3]
print(my_list)