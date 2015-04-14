#File modes
# r  : Opens file for reading (is the default).
# w  : Opens file for writing. Overwrites old or creates if doesn't exist.
# a  : Opens file for appending. Overwrites old or creates if doesn't exist.
# r+ : Opens file for reading and writing.
# w+ : Opens file for reading and writing. Overwrites old or creates if doesn't exist.
# a+ : Opens file for reading and appending. Overwrites old or creates if doesn't exist.

#Open the file for appending.
file_handle = open("sample1.txt", "a")

#Append to the file.
file_handle.write("Appended line.\n")

#Close the file.
file_handle.close()
