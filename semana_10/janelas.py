import tkinter

window = tkinter.Tk() #cria a janela
window.title('Luís 😁')
window.geometry('600x300')

#Criação de comandos pros botões:funções
def hello():
    print('O botão foi pressionado!')



#1 Etapa -> Criação do widget/elemnto
label = tkinter.Label(window, text='Isto é uma Label', font=('Arial', 20))
button = tkinter.Button(window,text='Pressione aqui!', command=hello)




#2 Etapa -> Posicionamento desse elemento na janela (pack, grid, place)

label.pack() # posicionando minha label na tela com método pack
button.pack()




window.mainloop() #mantém a janela aberta por meio de um loop eterno
print('Isso só vai rodar quando a janela for fechada')

#pip install tkinter