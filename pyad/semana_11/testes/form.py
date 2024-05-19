import tkinter
from tkinter import ttk

def buscar_dados():

    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    title = title_combobox.get()
    age = age_spinbox.get()
    nationality = nationality_combobox.get()

    reg_status = reg_status_var.get()
    

    numcourses = numcourses_spinbox.get()
    numsemester = numsemester_spinbox.get()

    print("First Name:", firstname)
    print("Last Name:", lastname)
    print("Title:", title)
    print("Age:", age)
    print("Nationality:", nationality)
    print("Registration Status:", reg_status)
    print("Terms and Conditions:", terms_check)
    print("Number of Completed Courses:", numcourses)
    print("Number of Completed Semesters:", numsemester)


window = tkinter.Tk()
window.title('Formulário')

#criamento de widgets
frame = tkinter.Frame(window) #vamos colocar tres linhas

user_info_frame = tkinter.LabelFrame(frame, text="Informações do Usuário")

first_name_label = tkinter.Label(user_info_frame, text="Nome")
last_name_label = tkinter.Label(user_info_frame, text='Sobrenome')

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)

title = tkinter.Label(user_info_frame, text='Título')
title_combobox = ttk.Combobox(user_info_frame, values=['', 'Sr.', 'Sra', 'Dr.'])

age_label = tkinter.Label(user_info_frame, text='Idade')
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18,to=110)

nationality_label = tkinter.Label(user_info_frame, text='Nacionalidade')
nationality_combobox = ttk.Combobox(user_info_frame, values=["Afeganistão", "Albânia", "Argélia", "Andorra", "Angola", "Argentina", "Armênia", "Austrália", "Áustria", "Azerbaijão", "Bahamas", "Bangladesh", "Barbados", "Bielorrússia", "Bélgica", "Belize", "Benin", "Butão", "Bolívia", "Bósnia e Herzegovina", "Botswana", "Brasil", "Brunei", "Bulgária", "Burkina Faso", "Burundi", "Camboja", "Camarões", "Canadá", "Cabo Verde", "Chade", "Chile", "China", "Colômbia", "Comores", "Congo", "Costa Rica", "Croácia", "Cuba", "Chipre", "República Checa", "Dinamarca", "Djibouti", "Dominica", "República Dominicana", "Timor Leste", "Equador", "Egito", "El Salvador", "Guiné Equatorial", "Eritreia", "Estônia", "Eswatini", "Etiópia", "Fiji", "Finlândia", "França", "Gabão", "Gâmbia", "Geórgia", "Alemanha", "Gana", "Grécia", "Granada", "Guatemala", "Guiné", "Guiné-Bissau", "Guiana", "Haiti", "Honduras", "Hungria", "Islândia", "Índia", "Indonésia", "Irã", "Iraque", "Irlanda", "Israel", "Itália", "Jamaica", "Japão", "Jordânia", "Cazaquistão", "Quênia", "Kiribati", "Coreia do Norte", "Coreia do Sul", "Kuwait", "Quirguistão", "Laos", "Letônia", "Líbano", "Lesoto", "Libéria", "Líbia", "Liechtenstein", "Lituânia", "Luxemburgo", "Madagascar", "Malawi", "Malásia", "Maldivas", "Mali", "Malta", "Ilhas Marshall", "Mauritânia", "Maurício", "México", "Micronésia", "Moldávia", "Mônaco", "Mongólia", "Montenegro", "Marrocos", "Moçambique", "Myanmar", "Namíbia", "Nauru", "Nepal", "Países Baixos", "Nova Zelândia", "Nicarágua", "Níger", "Nigéria", "Macedônia do Norte", "Noruega", "Omã", "Paquistão", "Palau", "Panamá", "Papua Nova Guiné", "Paraguai", "Peru", "Filipinas", "Polônia", "Portugal", "Catar", "Romênia", "Rússia", "Ruanda", "Samoa", "San Marino", "São Tomé e Príncipe", "Arábia Saudita", "Senegal", "Sérvia", "Seychelles", "Serra Leoa", "Cingapura", "Eslováquia", "Eslovênia", "Ilhas Salomão", "Somália", "África do Sul", "Espanha", "Sri Lanka", "Sudão", "Sudão do Sul", "Suriname", "Suécia", "Suíça", "Síria", "Taiwan", "Tajiquistão", "Tanzânia", "Tailândia", "Togo", "Tonga", "Trinidad e Tobago", "Tunísia", "Turquia", "Turcomenistão", "Tuvalu", "Uganda", "Ucrânia", "Emirados Árabes Unidos", "Reino Unido", "Estados Unidos", "Uruguai", "Uzbequistão", "Vanuatu", "Vaticano", "Venezuela", "Vietnã", "Iêmen", "Zâmbia", "Zimbábue"])

#posicionamento1
frame.pack()
user_info_frame.grid(row=0, column=0, padx=20, pady=20)

first_name_label.grid(row=0, column=0)
last_name_label.grid(row=0, column=1)

first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)

title.grid(row=0, column=2)
title_combobox.grid(row=1,column=2)

age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label.grid(row=2,column=1)
nationality_combobox.grid(row=3, column=1)

#loop de configuração

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


#Segunda frame

#widgets

courses_frame = tkinter.LabelFrame(frame)
registred_label = tkinter.Label(courses_frame, text="Status de Matrícula")

reg_status_var = tkinter.StringVar(value='Não Registrado')
registred_check = tkinter.Checkbutton(courses_frame, text='Currently Registred', variable=reg_status_var, onvalue='Registrado', offvalue='Não Registrado')

numcourses_label = tkinter.Label(courses_frame, text="# Cursos Completados")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numsemester_label = tkinter.Label(courses_frame, text="# Semestres Completados")
numsemester_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')


#loop de configuração

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)




#posicionamento 2
courses_frame.grid(row=1, column=0, sticky='news', padx=20, pady=20)
registred_label.grid(row=0, column=0)
registred_check.grid(row=1, column=0)
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1 )
numsemester_label.grid(row=0, column=2)
numsemester_spinbox.grid(row=1, column=2)

#frame termos e condições

terms_frame = tkinter.LabelFrame(frame, text='Termos e Condições')
terms_check_var = tkinter.StringVar(value='Não Concorda')
terms_check = tkinter.Checkbutton(terms_frame, text='Eu aceito os termos e condições', variable=terms_check_var, onvalue='Concorda', offvalue='Não Concorda')

#posicionamento 3


terms_frame.grid(row=2, column=0, sticky='news', padx=20, pady=20)
terms_check.grid(row=0, column=0)


#botao
button = tkinter.Button(frame, text='Enviar', command=buscar_dados) #quero que fique no frame principal
button.grid(row=3, column=0, sticky='news', pady=5)
window.mainloop()