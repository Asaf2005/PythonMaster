import tkinter as tk
from tkinter import Button

m = tk.Tk()



def insert():
    listbox.insert(tk.END, content.get())

def delete():
    listbox.delete(0)





frame = tk.Frame(m,bg='#80c1ff')
frame.place(relwidth=1,relheight=1)

content = tk.StringVar()
entry = tk.Entry(frame, bg='#A8A8A8', textvariable=content)
entry.pack()

insert_button = Button(frame, text='insert', bg='gray', fg = 'red', command=insert)
insert_button.pack()

del_button = Button(frame, text='delete', bg='gray', fg = 'red', command=delete)
del_button.pack()



listbox = tk.Listbox(frame)
listbox.pack()

m.mainloop()
