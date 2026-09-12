#Function	Description
#tk.Tk()	Initializes the main window.
#title("Window Title")	Sets the title of the window.
#configure(background)	Changes the background color of the window.
#geometry("widthxheight")	Sets the size of the window.
#mainloop()	Starts the Tkinter event loop to display the window.




import tkinter as tk


def on_button_click():
    print("Button Clicked")

root = tk.Tk()
root.title("Calculator")

my_button = tk.Button(root, text="click me", command=on_button_click)
my_button.pack()



root.configure(background="grey")
root.geometry("400x300")
root.mainloop()

