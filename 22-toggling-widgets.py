import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title('Toggling Widget')
window.geometry('900x600')

def toggle_widget_3():
    global label_visibility, text
    if label_visibility:
        text.set('')
        label_visibility = False
    else:
        text.set('Label')
        label_visibility = True
        label.pack(expand=True)

# def toggle_widget_2():
#     global label_visibility
#     if label_visibility:
#         label.grid_forget()
#         label_visibility = False
#     else:
#         label_visibility = True
#         label.grid(row=0, column=0)

# def toggle_widget():
#     # global label_visibility
#     if label_visibility:
#         label.place_forget()
#         label_visibility = False
#     else:
#         label_visibility = True
#         label.place(relx=0.5, rely=0.5)

# # Widgets
# button = ttk.Button(master=window, text='Toggle Label', command=toggle_widget)
# button.place(relx=0, rely=0.1)

# label_visibility = True
# label = ttk.Label(master=window, text='Label')
# label.place(relx=0.5, rely=0.5)

# Grid
# window.columnconfigure((0, 1), weight=1, uniform='a')
# window.rowconfigure(0, weight=1, uniform='a')

# Widgets
# label_visibility = True
# button = ttk.Button(master=window, text='Toggle Label', command=toggle_widget_2)
# button.grid(row=0, column=1)

# label_visibility = True
# label = ttk.Label(master=window, text='Label')
# label.grid(row=0, column=0)

# pack
label_visibility = True
text = tk.StringVar(value='Label')
label = ttk.Label(master=window, textvariable=text)
label.pack(expand=True)

label_visibility = True
button = ttk.Button(master=window, text='Toggle Label', command=toggle_widget_3)
button.pack()

# Run
window.mainloop()

