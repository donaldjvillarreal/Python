import re
from re2 import found

string = 'Here we test the start and the end'
regex1 = r'the$'
regex2 = r'end$'
regex3 = r'^we'
regex4 = r'^Here'
regex5 = r'^H.*d$'

result1 = re.search(regex1, string)
found(result1)
result2 = re.search(regex2, string)
found(result2)
result3 = re.search(regex3, string)
found(result3)
result4 = re.search(regex4, string)
found(result4)
result5 = re.search(regex5, string)
found(result5)