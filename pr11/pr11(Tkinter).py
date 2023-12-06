from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.ttk import Radiobutton
from tkinter import filedialog
def res_click():
    if simvol.get() == '+':
        r = int(f_numb.get()) + int(s_numb.get())
        res.configure(text=str(r))
    elif simvol.get() == '-':
        r = int(f_numb.get()) - int(s_numb.get())
        res.configure(text=str(r))
    elif simvol.get() == '*':
        r = int(f_numb.get()) * int(s_numb.get())
        res.configure(text=str(r))
    elif simvol.get() == '/':
        r = int(f_numb.get()) // int(s_numb.get())
        res.configure(text=str(r))

window = Tk()
window.title=('Kovalenko_Egor')
window.geometry('500x600')
tab_control = ttk.Notebook(window)
tab = ttk.Frame(tab_control)
tab_control.add(tab, text = 'Калькулятор')
calc = Label(tab)
calc.grid(column = 0, row = 0)
simvol = Combobox(calc, width = 5)
simvol['values'] = ('+', '-', '*', '/')
simvol.grid(column = 1, row = 0)
f_numb = Entry(calc, width = 10)
f_numb.grid(column = 0, row = 0)
s_numb = Entry(calc, width = 10)
s_numb.grid(column = 3, row = 0)
res_button = Button(calc, width = 5, text = ' = ', command = res_click)
res_button.grid(column = 5, row = 0)

def zhach_button():
    messagebox.showinfo('', 'Выберите: {} '.format(selected.get()))

tab_control.pack(expand = 2, fill = 'both')
res = Label(calc, width = 5)
res.grid(column = 4, row = 0)
chbox = ttk.Frame(tab_control)
tab_control.add(chbox, text = 'Checkbox')
selected = IntVar()
check1 = Radiobutton(chbox, text='Первый', value=1, variable=selected)
check1.grid(column = 0, row = 0)
check2 = Radiobutton(chbox, text='Второй', value=2, variable=selected)
check2.grid(column = 1, row = 0)
check3 = Radiobutton(chbox, text='Третий', value=3, variable=selected)
check3.grid(column = 2, row = 0)
check1 = Radiobutton(chbox, text='Первый', value=1, variable=selected)
check1.grid(column = 0, row = 0)
checkbutton = Button(chbox, text = 'Знак', width = 10, command = zhach_button)
checkbutton.grid(row=1)

def f_open():
    fi = filedialog.askopenfilename()
    if fi != ' ':
        with open(fi, 'r') as file:
            h = file.read()
            hd.delete('1.0', END)
            hd.insert('1.0',h)

def f_save():
    fi = filedialog.asksaveasfilename()
    if fi != ' ':
        h = hd.get('1.0',END)
        with open(h, 'w') as file:
            file.write(h)

txt_tab = ttk.Frame(tab_control)
tab_control.add(txt_tab, text = 'Действие')
hd = Text(txt_tab)
hd.grid(column = 0, row = 1, columnspan = 2)
obutton = ttk.Button(txt_tab, text = 'Открыть', command = f_open)
obutton.grid(column = 0, row = 0, padx = 10, sticky = NSEW)
sbutton = ttk.Button(txt_tab, text = 'Сохранить', command = f_save)
sbutton.grid(column = 1, row = 0, padx = 10, sticky = NSEW)
window.mainloop()
