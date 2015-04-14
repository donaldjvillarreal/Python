#replace() replaces each instance of one string with another.
print("Jack fell and Jack broke a leg".replace("Jack", "Jane"))

#find() finds the index on which the substring exists (-1 if it doesn't exist).
print("Where's Waldo?".find("Waldo"))

#isdigits() returns true if all the characters are digits.
print("1234f567".isdigit())

#The strip functions removes leading and ending whitespace.
print("      strip      ".strip(), "eol")
print("      strip      ".rstrip(), "eol")
print("      strip      ".lstrip(), "eol")

#Convert characters to unicode integer representation and back.
print(ord('c'))
print(chr(99))

#endswith() checks if the string ends with a substring.
extension_tuple = (".png", ".jpg", ".bmp")
file_list = ["dog.jpg", "cat.bmp", "worm.svg"]
for file in file_list:
    print(file.endswith(extension_tuple))

#And there are plenty more...
#https://docs.python.org/2/library/string.html