import requests

def get_exchange_rate(cambio_base, cambio_de_conversao):
    url = f'https://api.exchangerate-api.com/v4/latest/{cambio_base}'
    resposta = requests.get(url)
    data = resposta.json()
    exchange_rate = data['rates'][cambio_de_conversao]
    return exchange_rate

def convert_currency(total, exchange_rate):
    return total * exchange_rate

def main():
    cambio_base = input('Digite a moeda de base para a conversão ').upper()
    cambio_de_conversao = input('Digite a moeda a qual você deseja fazer a conversão ').upper()
    total = float(input('Digite o montante a ser convertido: '))

    exchange_rate = get_exchange_rate(cambio_base, cambio_de_conversao)
    converted_value = convert_currency(total, exchange_rate)

    print(f'{total} {cambio_base} é igual a {converted_value:.2f} {cambio_de_conversao}')

if __name__ == "__main__":
    main()