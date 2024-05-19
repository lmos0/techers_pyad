import csv

with open('cadastros.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for linha in csv_reader:
        print(linha)


