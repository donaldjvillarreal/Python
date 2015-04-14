sentence = "This Sentence Contains Several Words"

#split() will break up a string based on a delimiter.
word_list = sentence.split(' ')
print(word_list)

#join() connects a list of string with something between them.
print("xyz".join(word_list))

#upper() and lower() change the case of the characters.
print(sentence.upper())
print(sentence.lower())


command = "open my email"

#"in" will check if one string is contained in another.
if "email" in command:
    print("Something might happen here like opening the user's email.")
if "google" in command:
    print("This won't be printed.")

import webbrowser
user_input = input("What would you like to do?: ")
if "stackoverflow" in user_input:
    webbrowser.open("http://stackoverflow.com")