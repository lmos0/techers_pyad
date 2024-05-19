import requests
import tkinter


def movie(titulo):

    url = f"http://www.omdbapi.com/?t={titulo}&apikey=84a1f976"

    resposta = requests.get(url)
    data = resposta.json() #converte a resposta em um dicionário do python

    if data["Response"] == "True":
        return f'Título: {data['Title']}\nAno: {data['Year']}\nNota IMDB, {data['imdbRating']}\nDiretor: {data['Director']}\nGenêro: {data['Genre']}'


    return "Filme não encontrado ou servidor fora do ar!"


#criação da Janela/raiz/root
window = tkinter.Tk()
window.title('Informações sobre filmes')
window.config(bg='#332941')
window.geometry('400x350')
# window.resizable(False,False)

def update_text():
    movie_choice = entry.get()
    movie_info = movie(movie_choice)
    # text.delete("1.0", tkinter.END)
    # text.insert(tkinter.END,movie_info)
    label_info.config(text=movie_info)

#criar
frame = tkinter.Frame(window, bg='#3B3486')
button = tkinter.Button(frame, text='Consultar Filme', bg='#F8E559', command=update_text)
entry = tkinter.Entry (frame)
# text = tkinter.Text(frame, font=('Calibri', 13))
label = tkinter.Label(frame, text='Digite o título do Filme', font=('Arial', 14), justify='center', wraplength=400, background='#864AF9', fg='white')
label_info = tkinter.Label(frame, wraplength=380, justify='center', font=('Calibri',13))
#função de atualizar a tela


#posicionar widgets na tela
frame.pack(pady=15, padx=20)

label.pack(pady=5)
entry.pack(pady=5)
# text.pack()
label_info.pack(pady=5)
button.pack(pady=5)


window.mainloop()