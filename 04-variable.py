import tkinter as tk
from  tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('Button Pressed')
# window
window = tk.Tk()
window.title('Tkinter Variables')
window.geometry('600x500')

# tkinter variable
string_var = tk.StringVar(value='<empty>')

# widgets
label = ttk.Label(master=window, text='label', textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack(pady=5)

entry2 = ttk.Entry(master=window, textvariable=string_var)
entry2.pack(pady=5)

button = ttk.Button(master=window, text='button', command=button_func)
button.pack()

string_var_2 = tk.StringVar(value='Empty Text')

entry_1 = ttk.Entry(master=window, textvariable=string_var_2)
entry_1.pack()

entry_2 = ttk.Entry(master=window, textvariable=string_var_2)
entry_2.pack()

label_1 = ttk.Label(master=window, textvariable=string_var_2)
label_1.pack()

# run
window.mainloop()