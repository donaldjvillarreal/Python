import re
from re2 import found

string1 = 'aba'
string2 = 'abba'
string3 = 'abbba'
string4 = 'abbbba'
regex = r'ab{2,3}a'

result1 = re.search(regex, string1)
found(result1)
result2 = re.search(regex, string2)
found(result2)
result3 = re.search(regex, string3)
found(result3)
result4 = re.search(regex, string4)
found(result4)
