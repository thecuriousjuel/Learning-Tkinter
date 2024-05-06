import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title('Combo Box and Spin Box')
window.geometry('600x500')

# Combobox

items = ['Rice', 'Hilsa', 'Dum Aloo']
food_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(master=window, textvariable=food_string)
combo['values'] = items
combo.pack()

# Events
combo_label = ttk.Label(master=window, text='Selected Value:')
combo_label.pack()

combo.bind('<<ComboboxSelected>>', 
           lambda event: combo_label.configure(text = f'Selected Value: {food_string.get()}'))

# Spinbox
spin_int = tk.IntVar(value=12)
spin = ttk.Spinbox(master=window, 
                   from_= -6, 
                   to = 6, 
                   increment = 5, 
                   textvariable=spin_int, 
                   command=lambda: print(spin_int.get()))
# spin['value'] = [i for i in range(-5, 5)]
spin.pack()

spin.bind('<<Increment>>', lambda event: print('Up'))
spin.bind('<<Decrement>>', lambda event: print('Down'))

# Exercise

spin_box_values = [chr(ch+65) for ch in range(5)]
default_value = tk.StringVar(value=spin_box_values[0])
spin_box = ttk.Spinbox(master=window,
                       values=spin_box_values, 
                       textvariable=default_value)
spin_box.pack()

spin_box.bind('<<Decrement>>', lambda event: print(default_value.get()))

# Run
window.mainloop()