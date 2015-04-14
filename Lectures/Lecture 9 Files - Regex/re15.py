import re
from re2 import found

string1 = 'Squirrels are better than chipmunks'
string2 = 'There_are_no_spaces'
regex = r'.* are .*'

result1 = re.search(regex, string1)
found(result1)
result2 = re.search(regex, string2)
found(result2)