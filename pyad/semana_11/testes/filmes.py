import os
import tkinter
import requests


load_dotenv()

API_KEY = os.getenv("API_KEY")

def movie(m):
    url = f"http://www.omdbapi.com/?t={m}&apikey={API_KEY}"

    resposta = requests.get(url)
    print(resposta.status_code)
    data = resposta.json()  # converte a resposta em um dicionário do python

    if data["Response"] == "True":
        return f"Título: {data['Title']}\nAno: {data['Year']}\nNota IMDB: {data['imdbRating']}\nDiretor: {data['Director']}\nGênero: {data['Genre']}"

    else:
        return "Filme não encontrado ou servidor fora do ar!"

###configurações de janela
window = tkinter.Tk()
window.title("Informações sobre Filmes")
window.geometry("350x325")
window.configure(bg="")
window.resizable(False, False)

def update_label():
    user_choice = entry.get()
    text = movie(user_choice)
    label.config(text=text)


### configurações de widgets
frame = tkinter.Frame()
button = tkinter.Button(frame, text="Consultar Filmes", command=update_label)
entry = tkinter.Entry(frame)
label = tkinter.Label(frame, wraplength=380, justify="left", font=('Arial',12))


#posicionamento de elementos
frame.pack(pady=10)

entry.pack(pady=5)
label.pack(pady=5)
button.pack(pady=10)