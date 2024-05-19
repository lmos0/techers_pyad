import tkinter 

window = tkinter.Tk()
window.geometry('250x220')
window.title('Calculadora TECHERS')

calculation = ""

def add_to_calculation(tecla):
    global calculation #Utiliza a variável globalmente, de modo que qualquer alteração tenha implicações em todo código
    calculation +=str(tecla)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
    


def eval_calc():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0,'0')

def clear_field():
    global calculation
    calculation = ''
    text_result.delete(1.0, "end")


#calculadora tem que ter botões para as operações de + - * /, tem que ter um botão pra pagar e os números

# Criação dos Elementos (Entry e Button)

text_result = tkinter.Text(window, height=2, width=20, font=('Arial', 16))

btn_1 = tkinter.Button(window, text='1', width=5, font=('Arial', 12), command=lambda: add_to_calculation(1))
btn_2 = tkinter.Button(window, text='2', width=5, font=('Arial', 12), command=lambda: add_to_calculation(2))
btn_3 = tkinter.Button(window, text='3', width=5, font=('Arial', 12), command=lambda: add_to_calculation(3))
btn_4 = tkinter.Button(window, text='4', width=5, font=('Arial', 12), command=lambda: add_to_calculation(4))
btn_5 = tkinter.Button(window, text='5', width=5, font=('Arial', 12), command=lambda: add_to_calculation(5))
btn_6 = tkinter.Button(window, text='6', width=5, font=('Arial', 12), command=lambda: add_to_calculation(6))
btn_7 = tkinter.Button(window, text='7', width=5, font=('Arial', 12), command=lambda: add_to_calculation(7))
btn_8 = tkinter.Button(window, text='8', width=5, font=('Arial', 12), command=lambda: add_to_calculation(8))
btn_9 = tkinter.Button(window, text='9', width=5, font=('Arial', 12), command=lambda: add_to_calculation(9))
btn_0 = tkinter.Button(window, text='0', width=5, font=('Arial', 12), command=lambda: add_to_calculation(0))

btn_plus = tkinter.Button(window, text='+', width=5, font=('Arial', 12), command=lambda: add_to_calculation('+'))
btn_minus = tkinter.Button(window, text='-', width=5, font=('Arial', 12), command=lambda: add_to_calculation('-'))
btn_multiplication = tkinter.Button(window, text='x', width=5, font=('Arial', 12), command=lambda: add_to_calculation('*'))
btn_division = tkinter.Button(window, text='/', width=5, font=('Arial', 12), command=lambda: add_to_calculation('/'))

btn_result = tkinter.Button(window, text='=', width=5, font=('Arial', 12), command=eval_calc)
btn_delete = tkinter.Button(window, text='C', width=5, font=('Arial', 12), command=clear_field)

# Posicionamento dos elementos, usando .grid()
text_result.grid(columnspan=5)

btn_1.grid(row=1,column=1)
btn_2.grid(row=1,column=2)
btn_3.grid(row=1, column=3)
btn_4.grid(row=2,column=1)
btn_5.grid(row=2,column=2)
btn_6.grid(row=2,column=3)
btn_7.grid(row=3, column=1)
btn_8.grid(row=3, column=2)
btn_9.grid(row=3,column=3)
btn_0.grid(row=4, column=2)

btn_plus.grid(row=1, column=0)
btn_minus.grid(row=2, column=0)
btn_multiplication.grid(row=3, column=0)
btn_division.grid(row=4, column=0)

btn_delete.grid(row=4, column=1)

btn_result.grid(row=4, column=3)


window.mainloop()