#codigo a ser executado para cada item

'''frutas = {'maçã', 'banana', 'uva'}
for fruta in frutas:
    print(fruta)
'''
"""for i in range(8):
    print(f'Contagem: {i}')

for letra in "Python":
    print (letra)"""

'''#contador para soma dos numero 
soma = 0 #contador da soma dos 5 numeros 

#loop for para rodar 5x 
for soma_num in range(5):
   
# input dos numeros  
    numero = float(input("Digite um número: "))
    
#contador do loop dor range
    soma_num=1

#contador para somar ps numeros do contador soma
soma += numero
media = soma / 5

#exibe o resultado
print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")'''

'''soma = 0
quantidade_numeros = 5
 
print ("Digite 5 números POSITIVOS (ou 999 para parar o programa):")
for i in range(quantidade_numeros):
    numero = float(input(f"Digite o número {i + 1}: "))
   
    if numero == 999:
        print("Programa encerrado pelo usuário.")
        break
    elif numero < 0:
        print("Número inválido. Digite apenas números positivos.")
        continue
   
    soma += numero
 
print(f"A soma dos números é: {soma}")  
media = soma / quantidade_numeros
print(f"Soma numeros validos: {soma}")
print(f"Média dos números validos: {media}")
print ("Programa encerrado.")'''

'''#senha e comparar com while
#criar uma variavel com a senha 
senha = "123"
while True:
    digite_senha=input("Digite a senha ou 's' para encerrar: ")
    if digite_senha.lower() == "s":
        print("Programa encerrado.")
        break
    elif digite_senha.lower() == senha:
        print("Senha correta. Acesso concedido.")
        break
    else:
        print("Senha incorreta. Tente novamente.")'''
        
'''cupom="promo10"
 
while True:
    digite_cupom = input("Digite o cupom: 'S' para sair: ")
    if digite_cupom.lower() == "s":
        print("Saindo do programa...")
        break
    elif digite_cupom == cupom:
        print("Cupom válido! Acesso permitido.")
        break
    else:
        print("Cupom incorreto! Tente novamente ou digite 'S' para sair.")'''