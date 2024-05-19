import tkinter, pyshorteners



root = tkinter.Tk()
root.title('URL encurtador')
root.geometry('300x150')

def encurtador():
    encurtador = pyshorteners.Shortener()
    short_url = encurtador.tinyurl.short(longurl_entry.get())
    shorturl_entry.insert(0, short_url)


longurl_label = tkinter.Label(root,text='Enter Long URL')
longurl_entry = tkinter.Entry(root)
shorturl_label = tkinter.Label(root, text='link encurtado')
shorturl_entry = tkinter.Entry(root)
shorten_button = tkinter.Button(root,text='Enviar', command=encurtador)

longurl_label.pack()
longurl_entry.pack()
shorturl_label.pack()
shorturl_entry.pack()
shorten_button.pack()
root.mainloop()