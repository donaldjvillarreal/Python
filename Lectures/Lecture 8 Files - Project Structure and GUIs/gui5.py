from tkinter import Tk, PhotoImage, Button

container = Tk()

photo_image = PhotoImage(file="python.gif")
button = Button(image=photo_image)
button.pack()

container.mainloop()