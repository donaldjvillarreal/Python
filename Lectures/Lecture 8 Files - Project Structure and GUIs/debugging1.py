words = ['apple', 'apricot', 'banana', 'anvil', 'book', 'below', 'access']

for word in words:
    if word.startswith('a'):
        words.remove(word)
        print('Removing word starting with "a"')

print(words)