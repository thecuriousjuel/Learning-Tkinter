import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(event)

window = tk.Tk()
window.geometry('600x500')
window.title('Event Binding')

# Widgets
text = tk.Text(master=window)
text.pack()

entry = ttk.Entry(master=window)
entry.pack()

btn = ttk.Button(master=window, text='Button')
btn.pack()

# Events
# btn.bind('<Alt-KeyPress-a>', lambda event: print(f'An event: {event}'))
# window.bind('<Motion>', get_pos)
# window.bind('<KeyPress>', lambda event: print(f'Button Pressed: {event}'))

entry.bind('<FocusIn>', lambda event: print(f'Entry field: {event}'))
text.bind('<Shift-MouseWheel>', lambda event: print(f'Mousewheel: {event}'))

window.mainloop()