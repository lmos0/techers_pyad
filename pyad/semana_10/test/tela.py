import tkinter 
from tkinter import messagebox


def login():
    username = 'techers'
    password = 'coxinha123'
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo('Sucesso', 'Login efetuado com sucesso')
    else:
        messagebox.showerror('Erro', 'Usuário ou senha incorretos')



window = tkinter.Tk()
window.title("Tela de Login") #setar o título
window.geometry('340x440') #Declara o valor padrão
window.configure(bg='#333333') #se não colocar nada, ele vai usar a tela padrão

frame = tkinter.Frame(window, bg='#333333')


#Criar o widget
login_label = tkinter.Label(frame, text='Login', bg='#333333', fg="#FFFFFF", font=("Arial", 20)) #master é onde esse elemento estará vinculado
username_label = tkinter.Label(frame, text='Usuário', bg='#333333', fg="#FFFFFF", font=("Arial", 14))
username_entry = tkinter.Entry(frame, font=("Arial", 14))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 14))
password_label = tkinter.Label(frame, text="Senha", bg='#333333', fg="#FFFFFF", font=("Arial", 14))
login_button = tkinter.Button(frame, text='Logar', font=("Arial", 12), command=login, bg='#FFFFFF', fg='#333333')
#pack, place, grid -> PReciso posicionar na tela


#colocar o widget na tela
# label.pack()

frame.pack()

login_label.grid(row=0,column=0, columnspan=2, sticky='news', pady=40) #styck é para ocupar o espaço. news pontos cardeais
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
login_button.grid(row=3,column=0, columnspan=2, pady=25) #fala pra ele ocupar o espaço de 2 colunas. Tipo mergir cédulas
window.mainloop()
# print('oi')