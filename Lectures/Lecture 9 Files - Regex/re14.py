import re
from re2 import found

string = 'abababab'
regex = r'(ab)*'

result = re.search(regex, string)
found(result)
