import re

string = 'This is a string'

result = re.search(r'is', string)
if result:
    print("Found")
else:
    print("Not found")
    
result = re.search(r'pizza', string)
if result:
    print("Found")
else:
    print("Not found")
