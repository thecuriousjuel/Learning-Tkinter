import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title('Window')
# window.geometry('800x500+100+200')
window.iconbitmap('python.ico')

# Exercise
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()

display_width_half = display_width // 2
display_height_half = display_height // 2

window_width = 800
window_height = 500

window_width_half = window_width // 2
window_height_half = window_height // 2

left = display_width_half-window_width_half
top = display_height_half-window_height_half

window.geometry(f'{window_width}x{window_height}+{left}+{top}')

# Window sizes
# window.minsize(width=200, height=100)
# window.maxsize(width=1000, height=800)
# window.resizable(True, False)

# Screen Attributes
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# Window attributes
window.attributes('-alpha', 0.8)
# window.attributes('-topmost', True)
# window.attributes('-disable', True)
# window.attributes('-fullscreen', True)

# Title Bar
# window.overrideredirect(True)
grip = ttk.Sizegrip(master=window)
# grip.pack()
grip.place(relx=1.0, rely=1.0, anchor='se')

# Security Event
window.bind('<Escape>', lambda event: window.quit())

# Run
window.mainloop()

