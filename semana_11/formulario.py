import tkinter
from tkinter import ttk

def enviar_dados():
    contrato = variavel_contrato_check.get()
    if contrato == 'aceito':
        nome = nome_entrada.get()
        sobrenome = sobrenome_entrada.get()
        titulacao = titulo_combobox.get()
        idade = idade_spinbox.get()
        nacionalidade = nacionalidade_combobox.get()

        curso = curso_combobox.get()
        semestre = semestres_spinbox.get()

        
        matricula = variavel_matricula_check.get()

        print('Nome:', nome)
        print('Sobrenome:', sobrenome)
        print('Titulação:', titulacao)
        print('Idade:', idade)
        print('País de Origem:', nacionalidade)
        print('Cursando:', curso)
        print('Número de períodos completados:', semestre)

        print(contrato,matricula)
    else:
        print("Erro")



window = tkinter.Tk()
window.title('Formulário de Cadastro')


#criação dos widgets (Frames)
frame = tkinter.Frame(window)
info_usuario_frame = tkinter.LabelFrame(frame, text='Dados do Aluno')

#criação widgets
nome_label = tkinter.Label(info_usuario_frame, text='Nome')
sobrenome_label = tkinter.Label(info_usuario_frame,text='Sobrenome')

nome_entrada = tkinter.Entry(info_usuario_frame)
sobrenome_entrada = tkinter.Entry(info_usuario_frame)

titulo_label = tkinter.Label(info_usuario_frame, text='Título')
titulo_combobox = ttk.Combobox(info_usuario_frame, values=['','Sr.','Sra.', 'Mestre', 'Mestra', 'Dr.', 'Dra.'])

idade_label = tkinter.Label(info_usuario_frame, text='Idade')
idade_spinbox = tkinter.Spinbox(info_usuario_frame, from_=18, to=110)

nacionalidade_label = tkinter.Label(info_usuario_frame, text='Nacionalidade')
nacionalidade_combobox = ttk.Combobox(info_usuario_frame, values=["Afeganistão", "Albânia", "Argélia", "Andorra", "Angola", "Argentina", "Armênia", "Austrália", "Áustria", "Azerbaijão", "Bahamas", "Bangladesh", "Barbados", "Bielorrússia", "Bélgica", "Belize", "Benin", "Butão", "Bolívia", "Bósnia e Herzegovina", "Botswana", "Brasil", "Brunei", "Bulgária", "Burkina Faso", "Burundi", "Camboja", "Camarões", "Canadá", "Cabo Verde", "Chade", "Chile", "China", "Colômbia", "Comores", "Congo", "Costa Rica", "Croácia", "Cuba", "Chipre", "República Checa", "Dinamarca", "Djibouti", "Dominica", "República Dominicana", "Timor Leste", "Equador", "Egito", "El Salvador", "Guiné Equatorial", "Eritreia", "Estônia", "Eswatini", "Etiópia", "Fiji", "Finlândia", "França", "Gabão", "Gâmbia", "Geórgia", "Alemanha", "Gana", "Grécia", "Granada", "Guatemala", "Guiné", "Guiné-Bissau", "Guiana", "Haiti", "Honduras", "Hungria", "Islândia", "Índia", "Indonésia", "Irã", "Iraque", "Irlanda", "Israel", "Itália", "Jamaica", "Japão", "Jordânia", "Cazaquistão", "Quênia", "Kiribati", "Coreia do Norte", "Coreia do Sul", "Kuwait", "Quirguistão", "Laos", "Letônia", "Líbano", "Lesoto", "Libéria", "Líbia", "Liechtenstein", "Lituânia", "Luxemburgo", "Madagascar", "Malawi", "Malásia", "Maldivas", "Mali", "Malta", "Ilhas Marshall", "Mauritânia", "Maurício", "México", "Micronésia", "Moldávia", "Mônaco", "Mongólia", "Montenegro", "Marrocos", "Moçambique", "Myanmar", "Namíbia", "Nauru", "Nepal", "Países Baixos", "Nova Zelândia", "Nicarágua", "Níger", "Nigéria", "Macedônia do Norte", "Noruega", "Omã", "Paquistão", "Palau", "Panamá", "Papua Nova Guiné", "Paraguai", "Peru", "Filipinas", "Polônia", "Portugal", "Catar", "Romênia", "Rússia", "Ruanda", "Samoa", "San Marino", "São Tomé e Príncipe", "Arábia Saudita", "Senegal", "Sérvia", "Seychelles", "Serra Leoa", "Cingapura", "Eslováquia", "Eslovênia", "Ilhas Salomão", "Somália", "África do Sul", "Espanha", "Sri Lanka", "Sudão", "Sudão do Sul", "Suriname", "Suécia", "Suíça", "Síria", "Taiwan", "Tajiquistão", "Tanzânia", "Tailândia", "Togo", "Tonga", "Trinidad e Tobago", "Tunísia", "Turquia", "Turcomenistão", "Tuvalu", "Uganda", "Ucrânia", "Emirados Árabes Unidos", "Reino Unido", "Estados Unidos", "Uruguai", "Uzbequistão", "Vanuatu", "Vaticano", "Venezuela", "Vietnã", "Iêmen", "Zâmbia", "Zimbábue"])



#posicionando widgets na tela
frame.pack()

info_usuario_frame.grid(row=0,column=0, padx=20, pady=10)
nome_label.grid(row=0, column=1)
nome_entrada.grid(row=1, column=1)

sobrenome_label.grid(row=0, column=2)
sobrenome_entrada.grid(row=1, column=2)

titulo_label.grid(row=0, column=0)
titulo_combobox.grid(row=1,column=0)

idade_label.grid(row=2, column=0)
idade_spinbox.grid(row=3, column=0)

nacionalidade_label.grid(row=2, column=1)
nacionalidade_combobox.grid(row=3, column=1)


#loop de configuração
for widgets in info_usuario_frame.winfo_children():
    widgets.grid_configure(padx=10, pady=2)


####################
#Segundo Frame - Criação Widgets

curso_frame = tkinter.LabelFrame(frame, text='Informações sobre o curso')

matricula_label = tkinter.Label(curso_frame, text='Status de Matrícula')

variavel_matricula_check = tkinter.StringVar()
matricula_check = tkinter.Checkbutton(curso_frame, text='Atualmente Matriculado', variable=variavel_matricula_check, onvalue='matriculado', offvalue='não matriculado' )

curso_label = tkinter.Label(curso_frame, text='Curso de Graduação' )
curso_combobox = ttk.Combobox(curso_frame, values=["Administração", "Arquitetura e Urbanismo", "Artes Visuais", "Biologia", "Ciência da Computação", "Ciências Contábeis", "Ciências Sociais", "Direito", "Economia", "Educação Física", "Enfermagem", "Engenharia Civil", "Engenharia Elétrica", "Engenharia Mecânica", "Farmácia", "Filosofia", "Física", "Geografia", "História", "Jornalismo", "Letras", "Matemática", "Medicina", "Nutrição", "Pedagogia", "Psicologia", "Publicidade e Propaganda", "Química", "Relações Internacionais", "Serviço Social", "Sistemas de Informação", "Turismo"])

semestres_label = tkinter.Label(curso_frame, text='Períodos Cursados')
semestres_spinbox = tkinter.Spinbox(curso_frame, from_=1, to=10)

#Posicionamento do segundo bloco
curso_frame.grid(row=1, column=0, sticky='news', padx=20, pady=10)
matricula_label.grid(row=0, column=0)
matricula_check.grid(row=1, column=0)

curso_label.grid(row=0, column=1)
curso_combobox.grid(row=1, column=1)

semestres_label.grid(row=0, column=2)
semestres_spinbox.grid(row=1, column=2)

#Loop de configuração do segundo bloco
for widgets in curso_frame.winfo_children():
    widgets.grid_configure(padx=10, pady=2)


##### Terceiro Frame - Criação de Widgets

contrato_frame = tkinter.LabelFrame(frame, text='Termos e Condições')
variavel_contrato_check = tkinter.StringVar()
contrato_check = tkinter.Checkbutton(contrato_frame, text='Eu aceito os termos e condições do contrato', variable=variavel_contrato_check, onvalue='aceito', offvalue='recusado')

#Posicionamentos dos elementos do terceiro bloco
contrato_frame.grid(row=2, column=0, sticky='news', padx=20, pady=10)
contrato_check.grid(row=0, column=0)


#Configuração Botão

button = tkinter.Button(frame, text='Enviar Contrato', command=enviar_dados)
button.grid(row=3, column=0, sticky='news', pady=5) #news = centralizado

window.mainloop()