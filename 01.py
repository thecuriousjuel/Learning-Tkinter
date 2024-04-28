import tkinter as tk
from tkinter import ttk

def convert():
    print('convert')

# window
window = tk.Tk()
window.title('Miles to Kilometer')
window.geometry('300x150')

# title
title_label = ttk.Label(master=window,
                        text='Miles to Kilometer',
                        font='Calibri 20 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry = ttk.Entry(master = input_frame)
button = ttk.Button(master=input_frame, 
                    text='Convert',
                    command=convert)
entry.pack(side = 'left', padx=10)
button.pack(side = 'left')
input_frame.pack(pady=10)

# output
output_label = ttk.Label(master=window, 
                         text='Output',
                         font='Calibri 18 bold')
output_label.pack()
# run
window.mainloop()