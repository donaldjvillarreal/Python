import re
from re2 import found

string1 = 'Hello, Bob is my name'
string2 = 'Hello, Jane is my name'
string3 = 'Hello, Pete is my name'
regex = r'Hello, (Bob|Jane) is my name'

result1 = re.search(regex, string1)
found(result1)
result2 = re.search(regex, string2)
found(result2)
result3 = re.search(regex, string3)
found(result3)
