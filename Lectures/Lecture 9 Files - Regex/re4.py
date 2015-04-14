import re
from re2 import found

string1 = 'a3b'
string2 = 'akb'
string3 = 'aRb'
regex1 = r'a[0-9]b'
regex2 = r'a[a-z]b'
regex3 = r'a[0-9a-z]b'

result1 = re.search(regex1, string1)
found(result1)
result2 = re.search(regex1, string2)
found(result2)
result3 = re.search(regex1, string3)
found(result3)
print("")
result1 = re.search(regex2, string1)
found(result1)
result2 = re.search(regex2, string2)
found(result2)
result3 = re.search(regex2, string3)
found(result3)
print("")
result1 = re.search(regex3, string1)
found(result1)
result2 = re.search(regex3, string2)
found(result2)
result3 = re.search(regex3, string3)
found(result3)