import pandas as pd

df = pd.read_excel('aula1_duplicados.xlsx')
print(df.drop_duplicates(subset=['Nomes'])) #remove os elementos duplicados com base no nome