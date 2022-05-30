from tkinter import*
from tkinter import filedialog
def openFile():
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    print(filepath)
    print(file.read())
    file.close()
window = Tk()
button = Button(text="Open", command=openFile)
button.pack()
window.mainloop()