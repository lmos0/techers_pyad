import tkinter
from tkinter import messagebox #vai ativar as funções de avisos do tkinter

#Funcionalidades do código

def login():
    username = 'techers'
    password = 'coxinha123'
    
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo('Sucesso', 'Login efetuado com sucesso')
        print('Um usuário acabou de fazer login')
    
    else:
        messagebox.showerror('Falha no Login', "Usuário ou senha estão incorretas")
        print('Houve uma tentativa de login no sistema')


#### Criação da Janela Principal

window = tkinter.Tk() #Criamos a janela
window.title('Tela de Login')
window.geometry('340x440')
window.configure(bg='#333333') #configuramos as aparência da janela

####Criação dos widgets

frame = tkinter.Frame(window, bg='#333333') #criação da frame -> subjanela da janela principal, onde vamos vincular elementos

login_label = tkinter.Label(frame, text='Tela de Login', bg='#333333', fg='#FFFFFF', font=('Arial', 20)) #bg configura cor de fundo, fg configura parte frontal (fonte)
username_label = tkinter.Label(frame, text="Usuário", bg='#333333', fg='#FFFFFF', font=('Arial',14))
username_entry = tkinter.Entry(frame)
password_label = tkinter.Label(frame, text='Senha', bg='#333333', fg='#FFFFFF', font=('Arial' ,14))
password_entry = tkinter.Entry(frame, show='*') #Configurando para que o campo de entrada mostre astericos no lugar dos caracteres digitados
login_button = tkinter.Button(frame, text='Fazer Login', font=('Arial', 10), command=login)


#### Posicionamento dos widgets na janela

frame.pack() #Posicionamento da Frame, utilizando Pack para centralizar o widget(frame)

login_label.grid(row=0,column=0, columnspan=2, pady=40, sticky='news') #north, east, west, south. Styck orienta onde os elementos devem aderir na tela
username_label.grid(row=1,column=0)
username_entry.grid(row=1,column=1)
password_label.grid(row=2,column=0)
password_entry.grid(row=2,column=1)
login_button.grid(row=3,column=0, columnspan=2, pady=25) #columnspan determina quantas colunas o elemento deve ocupar na tela


window.mainloop() #Mantendo a janela aberta por meio de loop

