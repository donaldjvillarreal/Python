import os

#Rename a file.
os.rename('sample2.txt', 'sample3.txt')

#Make a directory.
os.mkdir('newdir')

#Change working directory.
os.chdir('newdir')

#Get the current working directory.
print(os.getcwd())

#Delete a directory.
os.chdir('..')
os.rmdir('newdir')

#Delete a file.
os.remove('sample3.txt')