from tkinter import *

root = Tk()

w = Canvas(root,height =300,width = 200)
w.pack()

w.create_rectangle(50,30,120,60,fill ='#ff9999')
w.create_rectangle(60,40,88,94,fill = '#ff3399')
w.create_line(50,40,30,50,fill = '#476042',width = 5)
w.create_line(90,50,60,40,fill = "#476042",width = 5)
print("success")
mainloop()


