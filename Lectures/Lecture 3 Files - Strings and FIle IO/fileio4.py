#Open files.
file_handle = open("sample1.txt", "r")
file_handle2 = open("sample2.txt", "w")

#Loop over each character.
while True:
    character = file_handle.read(1)
    if not character:
        break
    file_handle2.write(character)
    file_handle2.write('x')
    
#Close the files.
file_handle.close()
file_handle2.close()