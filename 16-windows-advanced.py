import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title('Windows Advanced')
window.geometry('900x600')

# Widgets
label1 = ttk.Label(master=window,
                   text='Label 1',
                   background='red')

label2 = ttk.Label(master=window,
                   text='Label 2',
                   background='blue')

# Pack
# label1.pack(side='left', expand=True, fill='y')
# label2.pack(side='top', expand=True, fill='y')

# Grid
# window.columnconfigure(0, weight = 1)
# window.columnconfigure(1, weight = 1)
# window.columnconfigure(2, weight = 2)
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)

# label1.grid(row=0, column=0, sticky='nsew')
# label2.grid(row=1, column=1, sticky='nsew', columnspan=2)

# Place
label1.place(x=100, y=200, width=200, height=100)
label2.place(relx=0.5, rely=0.5, relwidth=1, anchor='center')

# Run
window.mainloop()

