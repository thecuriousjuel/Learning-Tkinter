import ttkbootstrap as tk
from tkinter import ttk

# Window

class App(tk.Window):
    def __init__(self, title, height, width):
        super().__init__()
        self.title(title)
        self.geometry(f'{height}x{width}')
        self.minsize(height=600, width=600)

        Menu(self)
        Main(self)

        self.mainloop()


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=0.3, relheight=1)
        self.widgets()

    def widgets(self):
        menu_button_1 = ttk.Button(self, text='Button 1')
        menu_button_2 = ttk.Button(self, text='Button 2')
        menu_button_3 = ttk.Button(self, text='Button 3')

        menu_slider_1 = ttk.Scale(self, orient='vertical')
        menu_slider_2 = ttk.Scale(self, orient='vertical')

        self.columnconfigure((0, 1, 2), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

        menu_button_1.grid(row=0, column=0, sticky='nsew', columnspan=2)
        menu_button_2.grid(row=0, column=2, sticky='nsew')
        menu_button_3.grid(row=1, column=0, sticky='nsew', columnspan=3)

        menu_slider_1.grid(row=2, column=0, sticky='nsew', rowspan=2, pady=20)
        menu_slider_2.grid(row=2, column=2, sticky='nsew', rowspan=2, pady=20)

        Toggle(self)

        entry = ttk.Entry(self)
        entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor='center')


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)
        self.widget()

    def widget(self):
        Entry(self, 'red', 'Label 1', 'Button 1')
        Entry(self, 'blue','Label 2', 'Button 2')


class Toggle(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=4, column=0, sticky='nsew', columnspan=3)
        self.widgets()

    def widgets(self):
        menu_toggle_1 = ttk.Checkbutton(self, text='Check 1')
        menu_toggle_2 = ttk.Checkbutton(self, text='Check 2')

        menu_toggle_1.pack(side='left', expand=True)
        menu_toggle_2.pack(side='left', expand=True)


class Entry(ttk.Frame):
    def __init__(self, parent, bgcolor, label_text, button_text):
        super().__init__(parent)
        self.pack(expand=True, fill='both', side='left', padx=20, pady=20)
        self.bgcolor = bgcolor
        self.label_text = label_text
        self.button_text = button_text
        self.widget()

    def widget(self):
        label = ttk.Label(self, text=self.label_text, background=self.bgcolor)
        button = ttk.Button(self, text=self.button_text)

        label.pack(expand=True, fill='both')
        button.pack(expand=True, fill='both', pady=10)


App('Combined Layout Classes', 900, 600)

