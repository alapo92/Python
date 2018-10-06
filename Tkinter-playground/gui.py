from tkinter import *

root = Tk()


def callback():
    print("Click!")


one = Label(root, text="One", bg='black', fg='white')
one.pack()
two = Label(root, text="two", bg='white', fg='black')
two.pack(fill=X)
Three = Label(root, text="Three", bg='Green', fg='Blue')
Three.pack(side=LEFT, fill=Y)
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", command=callback, fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)
# theLabel = Label(root, text="This is too easy")
# theLabel.pack()
root.mainloop()

