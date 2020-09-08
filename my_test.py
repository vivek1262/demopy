from tkinter import *

root = Tk()

v = IntVar()
v.set(1)

languages = [("Python",1),("Perl",2),("Java",3),("C++",4),("C",5)]

def ShowChoice():
    print(v.get())

Label(root,text ="Programming language",padx = 10,justify = LEFT).pack()

for val, language in enumerate(languages):
    Radiobutton(root,text=language,padx = 20,variable=v,command=ShowChoice,value=val).pack(anchor=W)


root.mainloop()