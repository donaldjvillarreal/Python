from tkinter import Tk, Button, Label, Entry, RIGHT, LEFT, TOP, BOTTOM

container = Tk()

start_label = Label(container, text="Start:")
start_label.grid(row=0, column=0)

start_entry = Entry(container)
start_entry.grid(row=0, column=1)

end_label = Label(container, text="End:")
end_label.grid(row=1, column=0)

end_entry = Entry(container)
end_entry.grid(row=1, column=1)

range_label = Label(container, text="Nothing")
range_label.grid(row=2, columnspan=2)

def show_range():
    start = int(start_entry.get())
    end = int(end_entry.get())
    numbers = list(range(start, end))
    range_label['text'] = str(numbers)
    
button = Button(container, text="Get range", command=show_range)
button.grid(row=3, columnspan=2)

container.mainloop()
