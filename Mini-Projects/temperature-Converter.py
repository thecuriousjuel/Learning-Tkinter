import tkinter as tk
from tkinter import ttk

operations = {
    '°C_to_°C': lambda x: x,
    '°C_to_°F': lambda x: (x * (9/5)) + 32,
    '°C_to_K': lambda x: x + 273.15,
    '°F_to_°C': lambda x: (x - 32) * (5/9),
    '°F_to_K': lambda x: operations['°C_to_K'](operations['°F_to_°C'](x)),
    '°F_to_°F': lambda x: x,
    'K_to_°C': lambda x: x - 273.15,
    'K_to_°F': lambda x: operations['°C_to_°F'](operations['K_to_°C'](x)),
    'K_to_K': lambda x: x,
}

display_options = ['°C', '°F', 'K']
default_scale = display_options[0]

def helper_convert_1(scale_1):
    key = f'{scale_1}_to_{option_list_2_value.get()}'
    value = temp_input_var.get()
    converted_value = operations[key](value)
    temp_output_var.set(converted_value)

def helper_convert_2(scale_2):
    key = f'{scale_2}_to_{option_list_1_value.get()}'
    value = temp_output_var.get()
    converted_value = operations[key](value)
    temp_input_var.set(converted_value)

window = tk.Tk()
window.title('Temperator Converter')
window.geometry('500x150')
window.minsize(height=100, width=410)

top_frame = ttk.Frame(master=window)
mid_frame = ttk.Frame(master=window)
bottom_frame = ttk.Frame(master=window)

top_frame_label = ttk.Label(
    master=top_frame, text="Biswajit's Temperature Converter")

temp_input_var = tk.DoubleVar(value=0)
temperature_entry = ttk.Entry(master=mid_frame, textvariable=temp_input_var)

option_list_1_value = tk.StringVar()
option_list_1 = ttk.OptionMenu(mid_frame, option_list_1_value,
                               default_scale, *display_options, command=helper_convert_1)

equals = ttk.Label(master=mid_frame, text='=')

temp_output_var = tk.DoubleVar()
temperature_label = ttk.Label(master=mid_frame, textvariable=temp_output_var)

option_list_2_value = tk.StringVar()
option_list_2 = ttk.OptionMenu(mid_frame, option_list_2_value,
                               default_scale, *display_options, command=helper_convert_1)


top_frame.pack(expand=True, fill='both')
mid_frame.pack(expand=True, fill='both')
bottom_frame.pack(expand=True, fill='both')

top_frame_label.pack()
temperature_entry.pack(side='left', expand=True, fill='x', padx=10)
option_list_1.pack(side='left', expand=True, fill='both', padx=10)
equals.pack(side='left', expand=True, fill='both', padx=10)

temperature_label.pack(side='left', expand=True, fill='both', padx=10)
option_list_2.pack(side='left', expand=True, fill='both', padx=10)

window.mainloop()
