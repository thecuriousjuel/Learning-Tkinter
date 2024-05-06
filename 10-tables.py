import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title('Treeview')
window.geometry('500x600')

n = 10
letters = [chr(i+65) for i in range(n)]
numbers = [i for i in range(n)]

print(letters)
print(numbers)

table = ttk.Treeview(master=window, 
                     columns=('num', 'let'), 
                     show='headings')
table.heading('num', text='Numbers')
table.heading('let', text='Letters')
table.pack(fill='both', expand=True)

# table.insert(parent='', index=0, values=('John', 'Doe', 'JohnDoe@email.com'))

for i in range(n):
    table.insert(parent='', index=0, values=(numbers[i], letters[i]))

table.insert(parent='', index=tk.END, values=(50, 'GG'))

# Events
def item_select(_):
    selected  = table.selection()
    for sel in selected:
        t = table.item(sel)
        print(t['values'])

def delete_items(_):
    selected = table.selection()
    for sel in selected:
        t = table.item(sel)
        table.delete(sel)
        v1, v2 = t['values']
        numbers.remove(v1)
        letters.remove(v2)
        print(f'Deleted [{v1}-{v2}]')
    print(f'Numbers={numbers}')
    print(f'Letters={letters}')

# table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)

# Run
window.mainloop()

