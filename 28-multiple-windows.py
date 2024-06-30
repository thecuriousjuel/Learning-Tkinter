import tkinter as tk
from tkinter import ttk

# Window
class SubWindow(tk.Toplevel):
    def __init__(self, title, height, width):
        super().__init__()
        self.title(title)
        self.geometry(f'{width}x{height}')

class App(tk.Tk):
    def __init__(self, title, height, width):
        super().__init__()
        self.title(title)
        self.geometry(f'{width}x{height}')
        self.sub_window = None

    def widgets(self, title, height, width):
        def create_window():
            if self.sub_window is None:
                self.sub_window = SubWindow(title, height, width)

        def destroy_window():
            if self.sub_window is not None:
                self.sub_window.destroy()
                self.sub_window = None

        ttk.Button(text='Create a New Window', command=create_window).pack(pady=20)
        ttk.Button(text='Close the new Window', command=destroy_window).pack()

app = App(title='Multiple Windows', height=600, width=900)
app.widgets(title='Sub Window', height=500, width=500)

# Run
app.mainloop()
