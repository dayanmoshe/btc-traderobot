import requests
import time

# Exemplo de coleta de dados de preço de BTC
def coletar_preco_btc():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    resposta = requests.get(url)
    dados = resposta.json()
    preco_btc = dados['bitcoin']['usd']
    return preco_btc

def monitorar_btc():
    while True:
        preco = coletar_preco_btc()
        print(f'Preço atual do BTC: ${preco}')
        # Lógica para enviar alertas pode ser colocada aqui
        time.sleep(60)

if __name__ == "__main__":
    monitorar_btc()
