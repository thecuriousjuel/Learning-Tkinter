import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Buttons')
window.geometry('500x600')

# button
btn_str = tk.StringVar(value='Go')
button = ttk.Button(master=window, 
                    command=lambda: print('A basic button!'),
                    textvariable=btn_str)
button.pack()

# check button
check_var = tk.IntVar()
check = ttk.Checkbutton(window, 
                        text = 'checkbox 1',
                        variable=check_var,
                        command= lambda: print(check_var.get(), type(check_var.get())),
                        onvalue=10,
                        offvalue=-10)
check.pack()

radio_var= tk.StringVar()
radio_1 = ttk.Radiobutton(master=window, 
                          text='Radio Button 1',
                          value='radio 1',
                          variable=radio_var, 
                          command=lambda: print(radio_var.get())
                          )
radio_1.pack()

radio_2 = ttk.Radiobutton(master=window, 
                          text='Radio Button 2', 
                          value='radio 2',
                          variable=radio_var, 
                          command=lambda: print(radio_var.get()))
radio_2.pack()

# exercise

def fun1():
    print(c_btn.get())
    c_btn.set(False)

def fun2():
    print(r_btn.get())

c_btn = tk.BooleanVar()
checkbox = ttk.Checkbutton(master=window,
                           variable=c_btn,
                           text='Ex-Checkbox',
                           command=fun2)
checkbox.pack()

r_btn = tk.StringVar()
r1 = ttk.Radiobutton(master=window,
                     text='Radio A',
                     value='A',
                     variable=r_btn, 
                     command=fun1)
r1.pack()
r2 = ttk.Radiobutton(master=window,
                     text='Radio B',
                     value='B',
                     variable=r_btn,
                     command=fun1)
r2.pack()


# run
window.mainloop()