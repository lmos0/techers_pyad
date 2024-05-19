import pandas as pd

data = [ 
    ['Suíça', 0.962, 'Europa'],
    ['Noruega', 0.966, 'Europa'],
    ['Islândia', 0.959, 'Europa'],
    ['Emirados Árabes Unidos', 0.911, 'Ásia'],
    ['Rússia', 0.821, 'Europa' ],
    ['Brasil', 0.760, 'América do Sul'],
    ['Suriname', 0.690, 'América do Sul']
]

df = pd.DataFrame(data, columns=['País', 'IDH', 'Continente'])

df.to_csv('idh_mundial.csv', index=False)