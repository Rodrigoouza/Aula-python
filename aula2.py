# concatenação
"""#entrada de dados
nome = input ("Qual o nome ?")
meio = input ("Qual o seu nome do meio?")
sobrenome = input ("Qual o seu sobrenome?")
ultimo_nome = input ("qual o seu ultimo nome?")
#concatenação de nome completo
nome_completo = nome + " " + meio + " " + sobrenome + " " + ultimo_nome
print (nome_completo)"""

#exemplo
"""#fatiamento de strings
palavra = "Brasil ira jogar hj"
# fazendo o fatiamento 
print(palavra[0:3])
print(palavra[5:8])
print(palavra[-4:])"""
 #att
"""palavra = input("Digite uma palavra: ")
# fazendo o fatiamento 
print(palavra[0:3])
print(palavra[3:8])
print(palavra[2:5])
print(palavra[-5:-1])
"""
#declaração de variavel

"""palavra = "INVENCIVEL"

#fazendo a inverção

print (palavra.lower())
print (palavra.upper())

# cortando palavra com split

print (palavra.lower().split("c"))
print (palavra.upper().split("V"))"""

#exercico
'''palavra = input("Digite uma palavra: ")
print(palavra.lower())
print(palavra.lower().split("a"))'''

#calculo de IMC
"""peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Você está com peso normal.")
else:
    print("Você está acima do peso.")"""

#calculo de consumo de energia
"""quantidade_pessoas = int(input("Digite a quantidade de pessoas: "))
consumo = float(input("Digite o consumo de energia (kWh): "))
consumo_por_pessoa = consumo / quantidade_pessoas
print(f"O consumo por pessoa é: {consumo_por_pessoa} kWh")
if consumo_por_pessoa <= 50:
    print("O consumo por pessoa é baixo.")
elif consumo_por_pessoa > 50 and consumo_por_pessoa <= 100:
    print("O consumo por pessoa é moderado.")
else:
    if consumo_por_pessoa >= 150:
        print("O consumo por pessoa é alto (sobregarga).")"""

#importando biblioteca
#biblioteca match
'''import math

raio = float(input("Digite o raio do círculo: "))
area = math.pi * (raio ** 2)
print(f"A área do círculo é: {area:.2f}")'''

'''import math
raio = float(input("Digite o raio da esfera: "))
volume = (4/3) * math.pi * (raio ** 3)  
 
print(f"O volume da esfera é: {volume:.2f} unidades de volume")'''

#biblioteca random
"""import random
numero = random.randint(1, 9999)
print(f"O número sorteado é: {numero}")"""

import requests
 
# 1. Pedir para o usuário qual moeda ele quer consultar
# Usamos .upper() para garantir que o texto fique em letras maiúsculas (ex: usd vira USD)
moeda = input("Digite a sigla da moeda estrangeira (ex: USD, EUR, BTC): ").upper()
 
# 2. Definir a URL da API usando a moeda digitada
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
 
# 3. Fazer a requisição do tipo GET
resposta = requests.get(url)
 
# 4. Verificar se a requisição deu certo
if resposta.status_code == 200:
    dados = resposta.json()
   
    # A API retorna um dicionário onde a chave é a combinação das moedas (ex: USDBRL)
    chave_moeda = f"{moeda}BRL"
   
    # Buscamos os dados específicos daquela moeda
    detalhes = dados[chave_moeda]
   
    # Extraímos as informações que queremos exibir
    nome = detalhes['name']       # Nome completo da moeda (ex: Dólar Americano/Real Brasileiro)
    valor_atual = detalhes['bid'] # Valor de compra atual
    maximo = detalhes['high']     # Maior valor do dia
    minimo = detalhes['low']      # Menor valor do dia
   
    print("\n" + "="*40)
    print(f"Dados da Cotação ({moeda}):")
    print(f"Moeda: {nome}")
    print(f"Valor Atual: R$ {float(valor_atual):.2f}")
    print(f"Máxima do dia: R$ {float(maximo):.2f}")
    print(f"Mínima do dia: R$ {float(minimo):.2f}")
    print("="*40)
 
else:
    # Se der erro 404, provavelmente a sigla da moeda está errada
    print(f"\nErro ao buscar cotação. Verifique se a sigla '{moeda}' está correta.")
 