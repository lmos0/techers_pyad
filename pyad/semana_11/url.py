import tkinter as tk
import pyshorteners


#Criando a Janela
window = tk.Tk()
window.title('Encurtador de URL')
window.geometry('300x150')
window.configure(bg='')
window.resizable(False,False)

#Funções

def encurtador():
    encurtador = pyshorteners.Shortener()
    short_url = encurtador.tinyurl.short(urldefault_entry.get())
    urlshort_entry.insert(0, short_url)
   

#Criar os widgets/elementos que irão ficar dentro da nossa janela

urldefault_label = tk.Label(window, text='Digite o link aqui: ')
urldefault_entry = tk.Entry(window)

urlshort_entry = tk.Entry(window)
urlshort_label = tk.Label(window,text='URL encurtado:')

main_button = tk.Button(window, text='Enviar', command=encurtador, font=("Arial", 14), bg='pink')


#Posicionamentos dos widgets

urldefault_label.pack()
urldefault_entry.pack()

urlshort_label.pack()
urlshort_entry.pack()

main_button.pack()


window.mainloop()

