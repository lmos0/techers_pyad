import pandas as pd

df = pd.read_excel('aula_pandas.xlsx')

 #devolve os elementos de acordo com a lógica estabelecida, no caso idade >30

specific_name = df[df['Nomes'] == 'Laura'] #devolve a mesma lógica do Python, se houver mínima diferença entre as strings, ele vai ignorar.

searched_name = df[df['Nomes'].str.contains('Sa')] #devolve os elementos com nomes que contém fragmentos da string pesquisada

nomes_a_buscar = ['Juliana Ferreira', 'Pedro Santos'] 


# print(specific_name)
# print(searched_name)
# print(df[df['Nomes'].isin(nomes_a_buscar)]) #método isin verifica o conteúdo de uma lista e devolve as linhas que batem com os critérios de filtragem


# nova_planilha = df[df['Idades'] > 45].sort_values(by='Nomes', ascending=True)
# nova_planilha.to_csv('maiores_de_45.csv', index=False)

print(df.filter(items=['Nomes', 'Cidades']))