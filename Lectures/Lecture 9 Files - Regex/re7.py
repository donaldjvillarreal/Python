import re
from re2 import found

string1 = 'aa'
string2 = 'aba'
string3 = 'abba'
regex = r'ab+a'

result1 = re.search(regex, string1)
found(result1)
result2 = re.search(regex, string2)
found(result2)
result3 = re.search(regex, string3)
found(result3)
