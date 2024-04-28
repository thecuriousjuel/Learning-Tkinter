import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
def convert():
    in_miles = entry_int.get()
    in_kms = str(in_miles * 1.6) + ' Km(s)'
    output_string.set(in_kms)

# window
window = ttk.Window(themename='darkly')
window.title('Miles to Kilometer')
window.geometry('300x150')

# title
title_label = ttk.Label(master=window,
                        text='Miles to Kilometer',
                        font='Calibri 20 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, 
                    text='Convert',
                    command=convert)
entry.pack(side = 'left', padx=10)
button.pack(side = 'left')
input_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, 
                         font='Calibri 18 bold',
                         textvariable=output_string)
output_label.pack()
# run
window.mainloop()