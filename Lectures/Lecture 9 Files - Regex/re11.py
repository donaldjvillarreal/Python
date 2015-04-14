import re
from re2 import found

string1 = 'afa'
string2 = 'a4a'
string3 = 'aTa'
regex = r'a[^0-9]a'

result1 = re.search(regex, string1)
found(result1)
result2 = re.search(regex, string2)
found(result2)
result3 = re.search(regex, string3)
found(result3)
