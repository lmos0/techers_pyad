import pandas as pd

# df = pd.read_csv('world_population.csv')
df = pd.read_excel('aula1.xlsx')
df2 = pd.read_excel('aula1.xlsx', sheet_name='Numeros')
# df.info()

print(df.head(3)) #devolve os tres elementos head
print(df.tail(3)) #devolve os tres elementos tail
print(df.loc[0]) #devolve a linha 0
