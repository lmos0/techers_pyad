import tkinter 
import PyPDF2 
from tkinter import filedialog



window = tkinter.Tk() #Iniciei a janela principal
window.title('Leitor de Pdf')


def open_file():
    filename = filedialog.askopenfilename(title='Selecione o Arquivo', initialdir='C:\\Users\luis.santos\Documents\pyad\pyad\semana_12', filetypes=[('PDF files', '.pdf')])

    reader = PyPDF2.PdfReader(filename)
    for i in range(len(reader.pages)):
        current_text = reader.pages[i].extract_text()
        text_output.insert(tkinter.END, current_text)



#Criar elemento 
text_label = tkinter.Label(window, text='Texto extraído do PDF')
text_output = tkinter.Text(window)
text_button = tkinter.Button(window, text='Selecione arquivo PDF', command=open_file)


#Posicionar elementos tela
text_label.pack()
text_output.pack()
text_button.pack()


window.mainloop() # Mantendo o loop que faz a janela principal ficar aberta