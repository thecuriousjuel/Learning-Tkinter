import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title('Combined Layout')
window.geometry('900x600')
window.minsize(600, 600)

# Main layout widgets
menu_frame = ttk.Frame(window)
main_frame = ttk.Frame(window)

# main frame layout
menu_frame.place(x=0, y=0, relwidth=0.3, relheight=1)
main_frame.place(relx=0.3, y=0, relwidth=0.7, relheight=1)

# menu widgets
menu_button_1 = ttk.Button(menu_frame, text='Button 1')
menu_button_2 = ttk.Button(menu_frame, text='Button 2')
menu_button_3 = ttk.Button(menu_frame, text='Button 3')

menu_slider_1 = ttk.Scale(menu_frame, orient='vertical')
menu_slider_2 = ttk.Scale(menu_frame, orient='vertical')

toggle_frame = ttk.Frame(menu_frame)
menu_toggle_1 = ttk.Checkbutton(toggle_frame, text='Check 1')
menu_toggle_2 = ttk.Checkbutton(toggle_frame, text='Check 2')

entry = ttk.Entry(menu_frame)

# menu layout
menu_frame.columnconfigure((0, 1, 2), weight=1, uniform='a')
menu_frame.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

menu_button_1.grid(row=0, column=0, sticky='nsew', columnspan=2)
menu_button_2.grid(row=0, column=2, sticky='nsew')
menu_button_3.grid(row=1, column=0, sticky='nsew', columnspan=3)

menu_slider_1.grid(row=2, column=0, sticky='nsew', rowspan=2, pady=20)
menu_slider_2.grid(row=2, column=2, sticky='nsew', rowspan=2, pady=20)

toggle_frame.grid(row=4, column=0, sticky='nsew', columnspan=3)
menu_toggle_1.pack(side='left', expand=True)
menu_toggle_2.pack(side='left', expand=True)

entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor='center')

# main widget
entry_frame_1 = ttk.Frame(main_frame)
entry_frame_2 = ttk.Frame(main_frame)

main_label_1 = ttk.Label(entry_frame_1, text='Label 1', background='red')
main_label_2 = ttk.Label(entry_frame_2, text='Label 2', background='blue')

main_button_1 = ttk.Button(entry_frame_1, text='Button 1')
main_button_2 = ttk.Button(entry_frame_2, text='Button 2')

main_label_1.pack(expand=True, fill='both')
main_button_1.pack(expand=True, fill='both', pady=10)
entry_frame_1.pack(expand=True, fill='both', side='left', padx=20, pady=20)

main_label_2.pack(expand=True, fill='both')
main_button_2.pack(expand=True, fill='both', pady=10)
entry_frame_2.pack(expand=True, fill='both',side='left', padx=20, pady=20)

# ttk.Label(menu_frame, background='red').pack(expand=True, fill='both')
# ttk.Label(main_frame, background='blue').pack(expand=True, fill='both')


# Run
window.mainloop()
