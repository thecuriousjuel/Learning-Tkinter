import tkinter as tk
from tkinter import ttk

def fun(arg):
    print('Button pressed')
    print(arg.get())

def outer(arg):
    def inner():
        print('Button pressed')
        print(arg.get())
    return inner

window = tk.Tk()
window.title('Functions')
window.geometry('600x500')

entry_text = tk.StringVar(value='<enter value>')
entry = ttk.Entry(master=window,
                  textvariable=entry_text)
entry.pack(pady=10)

button = ttk.Button(master=window,
                    text='Enter',
                    command=outer(entry_text))
button.pack()

window.mainloop()