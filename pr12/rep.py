from tkinter import *
import json
import requests

def information():
    name = text.get()
    link = ("https://api.github.com/users/{name}")
    response = requests.get(link).json()
    keys = ['company','created_at','email','id','name','url']
    response_new = {}
    for i in keys:
        response_new[i] = response[i]
    with open('information.txt','w') as file:
        json.dump(response_new,file,indent=3)

window = Tk()
window.title('Поиск репозитория')
window.configure(background='purple')
window.geometry('355x400')
lbl = Label(window, text='Введите название репозитория', width=30, height=1, bg='red', font=45)
lbl.grid(row=0, column=1, padx=10)
text = Entry(window, width=20)
text.grid(column=1, row=1, pady=20)
button = Button(window,text='Получить информацию',width=30,height=1, command=information)
button.grid(row=3, column=1, pady=20)
window.mainloop()
