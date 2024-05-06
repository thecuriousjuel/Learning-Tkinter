import ttkbootstrap as tk
from tkinter import ttk

# Window
window = tk.Window()
window.title('Tabs')
window.geometry('500x600')

notebook = ttk.Notebook(master=window)

tab1 = ttk.Frame(master=notebook)
l1 = ttk.Label(master=tab1, text='Home')
l1.pack()

btn1 = ttk.Button(master=tab1, text='Enter')
btn1.pack()

tab2 = ttk.Frame(master=notebook)
l2 = ttk.Label(master=tab2, text='About')
l2.pack()

btn2 = ttk.Button(master=tab2, text='Exit')
btn2.pack()

tab3 = ttk.Frame(master=notebook)
btn3 = ttk.Button(master=tab3, text='More!')
btn3.pack()

btn4 = ttk.Button(master=tab3, text='More Data!')
btn4.pack()

notebook.add(tab1, text='Home')
notebook.add(tab2, text='About')
notebook.add(tab3, text='Info')
notebook.pack()

# Run
window.mainloop()

