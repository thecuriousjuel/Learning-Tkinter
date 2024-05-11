import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title('Pack Layout')
window.geometry('900x600')

# Widgets
label1 = ttk.Label(master=window,
                   text='First Label',
                   background='red')

label2 = ttk.Label(master=window,
                   text='Second Label',
                   background='blue')

label3 = ttk.Label(master=window,
                   text='Last of the Labels - This is for test purpose',
                   background='green')

button = ttk.Button(master=window,
                    text='Button')

# Layout
# label1.pack(side='top', expand=True, fill='both')
# label2.pack(side='top')
# label3.pack(side='top')
# button.pack(side='top', expand=True, fill='y')


# Exercise-1
# label1.pack(side='top', fill='x')
# label2.pack(side='top', expand=True)
# label3.pack(side='top', expand=True, fill='both')
# button.pack(side='top', fill='x')

# Exercise-2
label1.pack(side='top', expand=True, fill='both', padx=10, pady=10)
label2.pack(side='left', expand=True, fill='both')
label3.pack(side='top', expand=True, fill='both')
button.pack(side='top', expand=True, fill='both')

# Run
window.mainloop()

