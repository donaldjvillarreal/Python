import re
from re2 import found

string = 'Hello, my phone number is (123)456-7890 and my email is bob@example.com'
phone_regex = r'\(([0-9]{3})\)([0-9]{3})-([0-9]{4})'
email_regex = r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|edu)'

phone_result = re.search(phone_regex, string)
print(phone_result.group(1) + phone_result.group(2) + phone_result.group(3))

email_result = re.search(email_regex, string)
print(email_result.group())
