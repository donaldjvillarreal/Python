import re
from re2 import found

string = 'Squirrels are better than chipmunks'
regex = r'(.*) are (.*) (.*)'

result = re.search(regex, string)
print(result.group())
print(result.group(1))
print(result.group(2))
print(result.group(3))