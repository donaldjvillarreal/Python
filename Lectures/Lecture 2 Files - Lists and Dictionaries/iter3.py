from itertools import count, islice

for i in islice(count(), 5, 20):
    print(i)
