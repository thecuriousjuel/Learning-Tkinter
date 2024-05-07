import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title('Menu')
window.geometry('500x600')

# Menu
menu = tk.Menu(master=window)

# Sub Menu
file_menu = tk.Menu(master=menu, tearoff=False)
file_menu.add_command(label='New', command=lambda: print('New'))
file_menu.add_command(label='Open', command=lambda: print('Open'))
file_menu.add_separator()
file_menu.add_radiobutton(label='Selected', command=lambda: print('Radiobutton'))
menu.add_cascade(label='File', menu=file_menu)
window.configure(menu=menu)

# Another sub menu
help_menu = tk.Menu(master=menu, tearoff=False)
help_menu.add_command(label='Contact', command=lambda: print('Contact'))
help_menu_var = tk.StringVar()
help_menu.add_checkbutton(label='Check', 
                          onvalue='on', 
                          offvalue='off',
                          variable=help_menu_var,
                          command=lambda: print(help_menu_var.get()))
menu.add_cascade(label='Help', menu=help_menu)

# Menu Button
menu_button = ttk.Menubutton(master=window,
                             text='Menu Button')
menu_button.pack()

sub_menu_button = tk.Menu(master=menu_button,
                        tearoff=False)
sub_menu_button.add_command(label='Entry 1',
                            command=lambda: print('Entry 1'))
sub_menu_button.add_checkbutton(label='Check Button 1',
                            command=lambda: print('Check Button 1'))
menu_button.configure(menu=sub_menu_button)

# Exercise

exercise = tk.Menu(master=menu, tearoff=False)
exercise.add_command(label='Ex-1',
                         command=lambda: print('Ex-1'))
exercise.add_command(label='Ex-2',
                         command=lambda: print('Ex-2'))
menu.add_cascade(label='Exercise', menu=exercise)

sub_exercise = tk.Menu(master=menu, tearoff=False)
sub_exercise.add_command(label='Another Option!', 
                         command=lambda: print('Another Option!'))
exercise.add_cascade(label='Sub Menu',
                     menu=sub_exercise)

# Run
window.mainloop()

