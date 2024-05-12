import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title('Stacking Order')
window.geometry('900x600')

# Widgets
label1 = ttk.Label(master=window, text='Label 1', background='green')
label2 = ttk.Label(master=window, text='Label 2', background='red')

button1 = ttk.Button(master=window, text='Raise Label 1', command=lambda: label1.lift(aboveThis=label2))
button2 = ttk.Button(master=window, text='Raise Label 2', command=lambda: label2.lift())

# Layout
label1.place(x=50, y=100, width=300, height=150)
label2.place(x=150, y=60, width=140, height=100)

button1.place(relx=0.8, rely=1, anchor='se')
button2.place(relx=0.9, rely=1, anchor='se')

# Exercise
label3 = ttk.Label(master=window, text='Label 3', background='magenta')
button3 = ttk.Button(master=window, text='Raise Label 3', command=lambda: label3.lift())

label3.place(x=200, y=50, width=100, height=350)
button3.place(relx=1, rely=1, anchor='se')

# Run
window.mainloop()

