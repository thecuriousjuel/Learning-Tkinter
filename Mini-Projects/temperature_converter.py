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

class Calculator(tk.Tk):
    def __init__(self, title, height, width, min_height, min_width):
        super().__init__()
        self.title(title)
        self.geometry(f'{width}x{height}')
        self.minsize(height=min_height, width=min_width)

    def create_widgets(self):
        self.top_frame = ttk.Frame(master=self)
        self.mid_frame = ttk.Frame(master=self)
        self.bottom_frame = ttk.Frame(master=self)

        self.top_frame_label = ttk.Label(
            master=self.top_frame, text="Biswajit's Temperature Converter")

        self.temp_input_var = tk.DoubleVar(value=0)
        self.temperature_entry = ttk.Entry(master=self.mid_frame, textvariable=self.temp_input_var)

        self.option_list_1_value = tk.StringVar()
        self.option_list_1 = ttk.OptionMenu(self.mid_frame, self.option_list_1_value,
                                    default_scale, *display_options, command=self.helper_convert_1)

        self.equals = ttk.Label(master=self.mid_frame, text='=')

        self.temp_output_var = tk.DoubleVar()
        self.temperature_label = ttk.Label(master=self.mid_frame, textvariable=self.temp_output_var)

        self.option_list_2_value = tk.StringVar()
        self.option_list_2 = ttk.OptionMenu(self.mid_frame, self.option_list_2_value,
                                    default_scale, *display_options, command=self.helper_convert_2)

    def layout_widgets(self):
        self.top_frame.pack(expand=True, fill='both')
        self.mid_frame.pack(expand=True, fill='both')
        self.bottom_frame.pack(expand=True, fill='both')

        self.top_frame_label.pack()
        self.temperature_entry.pack(side='left', expand=True, fill='x', padx=10)
        self.option_list_1.pack(side='left', expand=True, fill='both', padx=10)
        self.equals.pack(side='left', expand=True, fill='both', padx=10)

        self.temperature_label.pack(side='left', expand=True, fill='both', padx=10)
        self.option_list_2.pack(side='left', expand=True, fill='both', padx=10)

    def helper_convert_1(self, scale_1):
        key = f'{scale_1}_to_{self.option_list_2_value.get()}'
        value = self.temp_input_var.get()
        converted_value = operations[key](value)
        self.temp_output_var.set(converted_value)

    def helper_convert_2(self, scale_2):
        key = f'{scale_2}_to_{self.option_list_1_value.get()}'
        value = self.temp_output_var.get()
        converted_value = operations[key](value)
        self.temp_input_var.set(converted_value)

calc = Calculator(title='Temperator Converter',
                  height=150,
                  width=500,
                  min_height=100,
                  min_width=410)
calc.create_widgets()
calc.layout_widgets()
calc.mainloop()
