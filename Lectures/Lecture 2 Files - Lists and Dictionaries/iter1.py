from itertools import chain

let = ['a', 'b', 'c']
num = [1, 2, 3]

for i in chain(num, let):
    print(i)

for i in zip(num, let):
    print(i)

