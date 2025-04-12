import requests
import time
import datetime  # Import datetime module

def get_btc_price_coingecko(currency='brl'):
    """Busca o preço atual do Bitcoin na API da CoinGecko."""
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin',
        'vs_currencies': currency
    }
    try:
        response = requests.get(url, params=params, timeout=10) # Adicionado timeout
        response.raise_for_status() # Verifica se houve erro na requisição (status code >= 400)
        data = response.json()
        # O retorno é algo como: {'bitcoin': {'brl': 350000.00}}
        price = data.get('bitcoin', {}).get(currency)
        return price
    except requests.exceptions.Timeout:
        print("Erro: Timeout ao conectar com a API da CoinGecko.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados da CoinGecko API: {e}")
        return None
    except Exception as e:
        print(f"Um erro inesperado ocorreu: {e}")
        return None

# Loop principal para exibir o preço a cada 20 segundos
if __name__ == "__main__":
    print("Iniciando monitoramento de preço do Bitcoin (CoinGecko)... Pressione Ctrl+C para sair.")
    while True:
        # Obtém a hora atual formatada
        # Using datetime.now() for current time
        now = datetime.datetime.now()
        current_time_str = now.strftime("%Y-%m-%d %H:%M:%S")

        price_brl = get_btc_price_coingecko('brl') # Ou 'usd' se preferir dólar

        if price_brl is not None:
            print(f"{current_time_str} - Preço BTC: R$ {price_brl:,.2f}") # Formatado para moeda BRL
        else:
            print(f"{current_time_str} - Não foi possível obter o preço.")

        # Espera 20 segundos
        try:
            time.sleep(20)
        except KeyboardInterrupt:
            print("\nMonitoramento interrompido.")
            break