import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title('Combined Layout using Functions')
window.geometry('400x600')

def frame_and_label(label_text, bg_color, button_text_1, button_text_2, button_text_3):
    frame = ttk.Frame(master=window)
    frame2 = ttk.Frame(master=frame)

    label = ttk.Label(master=frame, text=label_text, background=bg_color)
    button1 = ttk.Button(master=frame, text=button_text_1)
    button2 = ttk.Button(master=frame2, text=button_text_2)
    button3 = ttk.Button(master=frame2, text=button_text_3)

    frame.pack(expand=True, fill='both', pady=10)
    label.pack(expand=True, fill='both', side='left')
    button1.pack(expand=True, fill='both', side='left')
    frame2.pack(expand=True, fill='both', side='left')
    button2.pack(expand=True, fill='both')
    button3.pack(expand=True, fill='both')

labels = ['Label1', 'Label2', 'Label3', 'Label4', 'Label5']
colors = ['Red', 'Yellow', 'Blue', 'Green', 'bisque']
btn_texts_1 = ['Button', 'Click', 'Test', 'Launch', 'Exit']
btn_texts_2 = ['', '', '', '', '']
btn_texts_3 = 'exercise'

for label, color, btn_text_1, btn_text_2 in zip(labels, colors, btn_texts_1, btn_texts_2):
    frame_and_label(label, color, btn_text_1, btn_text_2, btn_texts_3)

# Run
window.mainloop()
