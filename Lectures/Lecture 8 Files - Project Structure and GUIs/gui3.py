from tkinter import Tk, Button, Label, Entry, LEFT

container = Tk()

name_label = Label(container, text="Name:")
name_label.pack(side=LEFT)

entry = Entry(container)
entry.pack(side=LEFT)

greeting_label = Label(container, text="No Greeting")
greeting_label.pack()

def say_hello():
    greeting_label['text'] = "Hello %s" % entry.get()

button = Button(container, text="Greeting", command=say_hello)
button.pack()

container.mainloop()
