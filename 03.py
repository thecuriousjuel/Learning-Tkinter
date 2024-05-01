import tkinter as tk
from tkinter import ttk

def btn_fn():
    # All the below 3 lines does the same thing
    # label.config(text=value)
    # label.configure(text=value)
    # label['text'] = value

    entry['state'] = 'disabled'
    # print(entry.configure())

def btn_fn1():
    entry['state'] = 'enabled'

window = tk.Tk()
window.title('Getting and Setting widgets')
window.geometry('300x200')

label = ttk.Label(master=window,text='Enter age')
entry = ttk.Entry(master=window)
disable_button = ttk.Button(master=window,
                            text='Disable', 
                            command=btn_fn)

enable_button = ttk.Button(master=window, 
                           text='Enable',
                           command=btn_fn1)

label.pack(pady=10)
entry.pack(pady=10)
disable_button.pack(pady=10)
enable_button.pack(pady=10)
window.mainloop()