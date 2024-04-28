import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def btn_func():
    print('Button Pressed!')

def print_hello():
    third_label_text.set('Hello World!')

window = ttk.Window(themename='journal')
window.title(string='Window and Widgets')
window.geometry('600x800')

# ttk label
top_label = ttk.Label(master=window, text='This is a text')
top_label.pack(pady=5)

# tk text
text_area = tk.Text(master=window,
                    height=30,
                    width=65)
text_area.insert(index='1.0', 
                 chars='This is a sample line\nThis is 2nd line')
text_area.pack(pady=5)

# tk entry

second_label_text = tk.StringVar(value='one line of text')
second_label = ttk.Entry(master=window, 
                         textvariable=second_label_text)
second_label.pack(pady=5)

third_label_text = tk.StringVar(master=window, 
                                value='')
third_label = ttk.Label(master=window,
                        textvariable=third_label_text)
third_label.pack(pady=5)

button2 = ttk.Button(text='Button', command=print_hello)
button2.pack(pady=5)
# ttk button

button = ttk.Button(text='A button',
                    command=btn_func)
button.pack(pady=5)

window.mainloop()