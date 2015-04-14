#Open the files.
file_handle = open("sample1.txt", "r")
file_handle2 = open("sample2.txt", "w")

#Get a list of the line strings.
file_line_list = file_handle.readlines()
print(file_line_list)

#Print the third line.
print(file_line_list[2])

#Change the second line.
file_line_list[1] = "This line has been changed!\n"
print(file_line_list)

#Save the new lines to the file.
file_handle2.writelines(file_line_list)

#Print each line.
for line in file_line_list:
    print(line)

#Close the files.
file_handle.close()
file_handle2.close()