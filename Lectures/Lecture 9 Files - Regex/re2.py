import re

def found(check):
    if check:
        print("Found")
    else:
        print("Not found")    

if __name__ == "__main__":
    string1 = 'a'
    string2 = 'b'
    string3 = 'c'
    regex = r'[ab]'

    result1 = re.search(regex, string1)
    found(result1)

    result2 = re.search(regex, string2)
    found(result2)

    result3 = re.search(regex, string3)
    found(result3)
