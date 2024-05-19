import pandas as pd

df = pd.read_excel('aula1.xlsx')

print(df[df['Idades'] > 30]) #devolve os elementos com idade maior que 30

specific_name = df[df['Nomes'] == 'Ana Oliveira'] #devolve os elementos com nome João

print(specific_name)

searching_names = ['João Pereira', 'Gabriel Rodrigues']
print(df[df['Nomes'].isin(searching_names)]) #devolve os elementos com nomes João Pereira e Gabriel Rodrigues
#isin é um método que verifica se os elementos estão na lista

search_fragments = df[df['Nomes'].str.contains('Ga')] #devolve os elementos com nomes que contém João
print(search_fragments) #str.contains é um método que verifica se a string contém o fragmento

print(df.filter(items=['Nomes', 'Idades'])) #devolve os elementos com os nomes e idades

# df[df['Idades'] > 30].to_excel('maiores_30.xlsx', index=False) #cria um arquivo excel com os elementos com idade maior que 30

print(df[df['Idades'] >30].sort_values(by='Idades', ascending=False)) #devolve os elementos com idade maior que 30 ordenados por idade