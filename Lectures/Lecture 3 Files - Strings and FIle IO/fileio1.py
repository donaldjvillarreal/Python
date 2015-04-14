#Open the file (for reading).
file_handle = open("sample1.txt")

#Read and print the content.
print(file_handle.read())

#Close the file (not really necessary here, but good practice).
file_handle.close()
