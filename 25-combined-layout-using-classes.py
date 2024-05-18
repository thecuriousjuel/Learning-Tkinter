import tkinter as tk
from tkinter import ttk

# Window

class App(tk.Tk):
    def __init__(self, title, height, width):
        super().__init__()
        self.title(title)
        self.geometry(f'{width}x{height}')

    def widgets(self, label_text, bg_color, button_text_1, button_text_2, button_text_3):
        Main_Frame(self, label_text, bg_color, button_text_1,
                   button_text_2, button_text_3)


class Main_Frame(ttk.Frame):
    def __init__(self, parent, label_text, bg_color, button_text_1, button_text_2, button_text_3):
        super().__init__(parent)
        self.pack(expand=True, fill='both', pady=10)
        self.widgets(label_text, bg_color, button_text_1,
                     button_text_2, button_text_3)

    def widgets(self, label_text, bg_color, button_text_1, button_text_2, button_text_3):
        label = ttk.Label(master=self, text=label_text, background=bg_color)
        button1 = ttk.Button(master=self, text=button_text_1)

        label.pack(expand=True, fill='both', side='left')
        button1.pack(expand=True, fill='both', side='left')

        Sub_Frame(self, button_text_2, button_text_3)


class Sub_Frame(ttk.Frame):
    def __init__(self, parent, button_text_2, button_text_3):
        super().__init__(parent)
        self.pack(expand=True, fill='both', side='left')
        self.widgets(button_text_2, button_text_3)

    def widgets(self, button_text_2, button_text_3):
        entry = ttk.Entry(master=self)
        button3 = ttk.Button(master=self, text=button_text_3)
        entry.pack(expand=True, fill='both')
        button3.pack(expand=True, fill='both')

labels = ['Label1', 'Label2', 'Label3', 'Label4', 'Label5']
colors = ['Red', 'Yellow', 'Blue', 'Green', 'bisque']
btn_texts_1 = ['Button', 'Click', 'Test', 'Launch', 'Exit']
btn_texts_2 = ['', '', '', '', '']
btn_texts_3 = 'exercise'

app = App(title='Combined Layout using Classes', height=600, width=400)

for label, color, btn_text_1, btn_text_2 in zip(labels, colors, btn_texts_1, btn_texts_2):
    app.widgets(label, color, btn_text_1, btn_text_2, btn_texts_3)

app.mainloop()
