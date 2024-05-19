import tkinter

window = tkinter.Tk()
window.title('Tela de Login')
window.geometry('340x440')

def hello_world():
    print('Hello World')

label = tkinter.Label(window, text='Login', font=('Arial', 20))
button = tkinter.Button(window, text='Logar', font=('Arial', 12), command=hello_world)

#colocar na janela
label.pack()
button.pack()

window.mainloop()

