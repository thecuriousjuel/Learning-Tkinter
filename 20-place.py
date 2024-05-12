import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title('Place')
window.geometry('900x600')

# Widgets
label1 = ttk.Label(master=window, text='Label 1', background='red')
label2 = ttk.Label(master=window, text='Label 2', background='blue')
label3 = ttk.Label(master=window, text='Label 3', background='green')
button = ttk.Button(master=window, text='Button')

# Layout
label1.place(x=0, y=0, width=300, height=50)
label2.place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.3, anchor='center')
label3.place(x=450, y=300, anchor='center', width=180, height=180)
button.place(relx=1, rely=1, anchor='se')

# Frame
frame = ttk.Frame(window)
label4 = ttk.Label(master=frame, text='Label 4', background='yellow')
button2 = ttk.Button(master=frame, text='Button')

frame.place(relx=0, rely=0, relwidth=0.3, relheight=1)
label4.place(relx=0, rely=0, relheight=0.5, relwidth=1)
button2.place(relx=0, rely=0.5, relheight=0.5, relwidth=1)

# Exercise
label5 = ttk.Label(master=window, text='Label 5', background='magenta')
label5.place(relx=0.5, rely=0.5, anchor='center', height=200, relwidth=0.5)

# Run
window.mainloop()

