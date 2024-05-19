import pandas as pd

df = pd.read_excel('aula_pandas.xlsx')
df2 = pd.read_csv('idh_mundial.csv')
print(df.tail(3)) # acessar informações no final da tabela. O Argumento (x) determina a quantidade de linhas a ser acessada

print(df.head(5)) # acessar informações no início da tabela. O Argumento (x) determina a quantidade de linhas a ser acessada

print(df.loc[3]) #acessar informações referentes a linha específica de um dataframe. Usa-se [] colchetes para colocar o index

