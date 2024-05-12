import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title('Grids')
window.geometry('900x600')


# Widgets
label1 = ttk.Label(master=window, text='Label 1', background='red')
label2 = ttk.Label(master=window, text='Label 2', background='blue')
label3 = ttk.Label(master=window, text='Label 3', background='green')
label4 = ttk.Label(master=window, text='Label 4', background='yellow')

button1 = ttk.Button(master=window, text='Button 1')
button2 = ttk.Button(master=window, text='Button 2')

entry = ttk.Entry(master=window)


# Define a grid
window.columnconfigure((0,1,2), weight=1, uniform='a')
window.columnconfigure(3, weight=2, uniform='a')
window.rowconfigure((0,1,2), weight=1, uniform='a')
window.rowconfigure(3, weight=3, uniform='a')


# Place
label1.grid(row=0, column=0, sticky='nswe')
label2.grid(row=1, column=1, sticky='nswe', rowspan=3)
label3.grid(row=1, column=0, sticky='nswe', columnspan=3, padx=20, ipady=10)
label4.grid(row=3, column=3, sticky='se')

# Exercise
button1.grid(row=0, column=3, sticky='nsew')
button2.grid(row=2, column=2, sticky='nsew')
entry.grid(row=2, column=3, rowspan=2, sticky='ew')

# Run
window.mainloop()

