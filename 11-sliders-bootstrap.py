# import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import ttkbootstrap as tk
# Window
window = tk.Window()
window.title('Sliders')
window.geometry('500x800')

# Slider
scale_var = tk.IntVar(value=15)
scale = ttk.Scale(master=window,
                  command=lambda x: print(f'Sliding! {x} : {scale_var.get()}'),
                  from_=25*4,
                  to = 0,
                  length=300,
                  orient='horizontal',
                  variable=scale_var)
scale.pack()

# Progress bar
# progress_var = tk.IntVar(value=15)
progress = ttk.Progressbar(master=window,
                           variable=scale_var,
                           maximum=25,
                           orient='horizontal',
                           mode='indeterminate',
                           length=400)
progress.pack()
# progress.start(1000)
progress.stop()


scrolled_text = scrolledtext.ScrolledText(master=window,
                                          width=100,
                                          height=10)
scrolled_text.pack()

# Exercise
pbar_var = tk.IntVar()
pbar = ttk.Progressbar(master=window,
                       orient='horizontal',
                       mode='determinate',
                       variable=pbar_var)
pbar.pack()
pbar.start()

label = tk.Label(master=window,
                 textvariable=pbar_var)
label.pack()

# scale_slider_var = tk.DoubleVar(value=20)
scale_slider = ttk.Scale(master=window,
                         length=200,
                         from_= 0,
                         to=100,
                         command=lambda x: print(x),
                         variable=pbar_var)
scale_slider.pack()




# Run
window.mainloop()

