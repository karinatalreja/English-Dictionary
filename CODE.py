from tkinter import *
from PyDictionary import PyDictionary

dictionary = PyDictionary
root = Tk()
root.geometry("400x400")
root.title("ËNGLISH DICTIONARY USING PYTHON API")

def dict():
    list1 = dictionary.meaning(word.get())['Noun'][0]
    tfield.insert(INSERT, list1)
        
    
    

label = Label(root, text = "DICTIONARY", fg = "Blue")
label.pack()

frame = Frame(root)
Label(frame, text="Type Word", font=("Helvetica 15 bold")).pack(side=LEFT)
word=Entry(frame, font="Helvetica 14")
word.pack()
frame.pack(pady=10)


frame1=Frame(root)
Label(frame1, text="Meaning:-", font=("Helvetica 15 bold")).pack(side=LEFT)
meaning=Label(frame1, text="", font=("Helvetica 12"))
meaning.pack()
frame1.pack(pady=10)

tfield = Text(width = 40, height = 20)
tfield.pack()

Button(root, text="Submit", font=("Helvetica 15 bold"), command=dict).pack()


root.mainloop()



    

