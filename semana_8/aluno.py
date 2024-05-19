#1. Crie uma classe Aluno com os atributos nome, matricula, curso e notas. Implemente um método calcular_media() que retorna a média das notas do aluno.

class Aluno:
    def __init__(self,nome:str,matricula:str,curso:str,notas:list):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = notas

    def calcular_media(self):
        media = sum(self.notas) / len(self.notas)
        return media


aluno1 = Aluno('João', '1234', "Ciências da Computação", [8,6,10,9,4])

aluno2 = Aluno('Élton','4321', 'Medicina', [7,8,9,9,3])
print(aluno2.calcular_media())
