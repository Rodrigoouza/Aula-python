import requests
 
Quantidade_de_Moedas = int(input("Digite a quantidade de moedas que deseja consultar: "))
moeda = input("Digite a sigla da moeda estrangeira (ex: USD, EUR, BTC): ").upper()
 
conversao = requests.get(f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL")
valor_convertido_USD = Quantidade_de_Moedas * float(conversao.json()[f"{moeda}-USD"]['bid'])
valor_convertido_BTC = Quantidade_de_Moedas * float(conversao.json()[f"{moeda}-BTC"]['bid'])
valor_convertido_EUR = Quantidade_de_Moedas * float(conversao.json()[f"{moeda}-EUR"]['bid'])
 
 
 
 
# Vamos extrair os valores ('bid') com segurança
bid_BRL = float(dados[f"{moeda}BRL"]['bid'])
bid_BTC = float(dados[f"{moeda}BTC"]['bid'])
bid_EUR = float(dados[f"{moeda}EUR"]['bid'])
 
'''# 3. Realizamos os cálculos
valor_convertido_BRL = Quantidade_de_Moedas * bid_BRL
valor_convertido_BTC = Quantidade_de_Moedas * bid_BTC
valor_convertido_EUR = Quantidade_de_Moedas * bid_EUR
'''
# 2. Definir a URL da API usando a moeda digitada
 
 
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
 
# 2. Convertemos para JSON
resposta = requests.get(url)
dados = resposta.json()
 
# 3. Fazer a requisição do tipo GET
resposta = requests.get(url)
 
# 4. Verificar se a requisição deu certo
if resposta.status_code == 200:
    dados = resposta.json()
   
    # A API retorna um dicionário onde a chave é a combinação das moedas (ex: USDBRL)
    chave_moeda = f"{moeda}BRL"
   
    # Buscamos os dados específicos daquela moeda
    detalhes = dados[chave_moeda]
    nome = detalhes['name']       # Nome completo da moeda (ex: Dólar Americano/Real Brasileiro)
    valor_atual = detalhes['bid'] # Valor de compra atual
 
 
#Resultado da conversão de moedas
 
print("\n" + "="*40)
print(f"Moeda: {nome}")
print(f"Dados da Cotação ({moeda}):")
print(f"Valor Atual: R$ {float(valor_atual):.2f}")
print(f"convertido para BTC é: BTC ₿ {valor_convertido_BTC:.6f}")
print(f"convertido para EUR é: EUR € {valor_convertido_EUR:.2f}")
print(f"convertido para USD: R$ {valor_convertido_USD:.2f}")
print("="*40)
 