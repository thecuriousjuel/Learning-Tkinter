import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title('Frames and Parenting')
window.geometry('500x600')

frame = ttk.Frame(master=window,
                  width=200,
                  height=200,
                  borderwidth=10,
                  relief=tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side='left')

label1 = tk.Label(master=frame, 
                 text='Label in Frame')
label1.pack()

label2 = tk.Label(master=window,
                  text='Label outside Frame')
label2.pack(side='left')

frame2 = ttk.Frame(master=window)
frame2.pack(side='right')

label3 = ttk.Label(master=frame2,
                   text='Another Label')
label3.pack()

btn = ttk.Button(master=frame2,
                 text='Button')
btn.pack()

entry = ttk.Entry(master=frame2)
entry.pack()


# Run
window.mainloop()

