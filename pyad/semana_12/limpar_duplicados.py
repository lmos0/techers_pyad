import pandas as pd

df = pd.read_excel('aula_pandas.xlsx')
print(df)

print(df.drop_duplicates(['Nomes']))