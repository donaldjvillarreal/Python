from tkinter import Tk, Button, Label, Entry

def add():
	num1 = first_entry.get()
	num2 = last_entry.get()
	if (first_entry.get() == ""):
		num1 = 0.
	if (last_entry.get() == ""):
		num2 = 0.
	range_label['text'] = str(float(num1) + float(num2))

def sub():
	num1 = first_entry.get()
	num2 = last_entry.get()
	if (first_entry.get() == ""):
		num1 = 0.
	if (last_entry.get() == ""):
		num2 = 0.
	range_label['text'] = str(float(num1) - float(num2))

def mult():
	num1 = first_entry.get()
	num2 = last_entry.get()
	if (first_entry.get() == ""):
		num1 = 0.
	if (last_entry.get() == ""):
		num2 = 0.
	range_label['text'] = str(float(num1) * float(num2))

def div():
	num1 = first_entry.get()
	num2 = last_entry.get()
	if (first_entry.get() == ""):
		num1 = 0.
	if (last_entry.get() == ""):
		num2 = 0.
	range_label['text'] = str(float(num1) / float(num2))

container = Tk()

first_entry = Entry(container)
first_entry.grid(row=0, columnspan=4)

last_entry = Entry(container)
last_entry.grid(row=1, columnspan=4)

button = Button(container, text="+", command=add)
button.grid(row=2, column=0)
button = Button(container, text="-", command=sub)
button.grid(row=2, column=1)
button = Button(container, text="*", command=mult)
button.grid(row=2, column=2)
button = Button(container, text="/", command=div)
button.grid(row=2, column=3)

range_label = Label(container, text="0")
range_label.grid(row=3, columnspan=4)
    


container.mainloop()
