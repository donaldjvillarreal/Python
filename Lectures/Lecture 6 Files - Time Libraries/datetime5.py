import datetime

now = datetime.datetime.now()

print(now)
print(now.ctime())
print(now.strftime("Year: %Y Month: %m Day: %d Hour: %H Minute: %M and Second: %S"))
print(now.strftime("%A %B %I%p"))

# Format reference: http://strftime.org/