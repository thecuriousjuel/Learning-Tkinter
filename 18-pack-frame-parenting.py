import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title('Pack Frame Parenting')
window.geometry('900x600')

top_frame = ttk.Frame(master=window)
bottom_frame = ttk.Frame(master=window)
exersice_frame = ttk.Frame(master=bottom_frame)

# Widgets
label1 = ttk.Label(master=top_frame,
                   text='First Label',
                   background='red')

label2 = ttk.Label(master=top_frame,
                   text='Second Label',
                   background='blue')

label3 = ttk.Label(master=window,
                   text='Third Label',
                   background='green')

label4 = ttk.Label(master=bottom_frame,
                   text='Fourth Label',
                   background='orange')

button1 = ttk.Button(master=bottom_frame,
                     text='Button 1')

button2 = ttk.Button(master=bottom_frame,
                     text='Button 2')

button3 = ttk.Button(master=exersice_frame,
                     text='Button 3')

button4 = ttk.Button(master=exersice_frame,
                     text='Button 4')

button5 = ttk.Button(master=exersice_frame,
                     text='Button 5')

# Top layout
label1.pack(fill='both', expand=True)
label2.pack(fill='both', expand=True)
top_frame.pack(fill='both', expand=True)

# Middle layout
label3.pack(expand=True)


# Bottom Left layout
button1.pack(side='left', expand=True, fill='both')
label4.pack(side='left', expand=True, fill='both')
button2.pack(side='left', expand=True, fill='both')
bottom_frame.pack(expand=True, fill='both', padx=20, pady=20)


# Bottom Right layout
button3.pack(expand=True, fill='both')
button4.pack(expand=True, fill='both')
button5.pack(expand=True, fill='both')
exersice_frame.pack(side='left',expand=True, fill='both')


# Run
window.mainloop()

