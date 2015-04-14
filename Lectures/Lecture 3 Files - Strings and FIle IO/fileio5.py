#Open file.
file_handle = open("sample1.txt")

#Get the first line.
line_one = file_handle.readline()
print(line_one)

#Get the first line.
line_two = file_handle.readline()
print(line_two)
    
#Close the file.
file_handle.close()
