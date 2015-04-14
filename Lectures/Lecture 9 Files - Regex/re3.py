import re
from re2 import found

string1 = 'grey'
string2 = 'gray'
string3 = 'gruy'
regex = r'gr[ae]y'

result1 = re.search(regex, string1)
found(result1)

result2 = re.search(regex, string2)
found(result2)

result3 = re.search(regex, string3)
found(result3)