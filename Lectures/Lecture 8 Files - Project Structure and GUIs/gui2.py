from tkinter import Tk, Button

def simple_callback():
    print("Hello world")

container = Tk()

button = Button(container, text="Say hello", command=simple_callback) # Create a button
button.pack() # Add the button to the top container

container.mainloop()
