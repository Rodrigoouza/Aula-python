'''soma = 0
quantidade_Peças= 5
print ("digite o peso das peças (digite 999 para encerrar):")
for i in range(quantidade_Peças):
    peso = float(input(f"Digite o peso da peça {i + 1}: "))
    
    if peso == 999:
        print("Processamento encerrado.")
        break

    elif peso<=0 or peso <50:
        print("Peça descartada por peso inválido. Pulando para próxima peça....")
        continue
    soma += peso

    print(f"Peso da peça {i + 1}: {peso}")

print(f"Soma dos pesos das peças aceitas: {soma}")
print(f"Média de peso das peças aceitas: {soma / quantidade_Peças if quantidade_Peças > 0 else 0}")'''

'''contador = 1 #variavel de inicio
while contador <= 5:
    print(contador)
    contador += 1'''

'''while True:
    resposta = input("Digite a palavra secreta para sair do loop: ")
    if resposta == "sair":
        print("Senha correta! Saindo do loop...")
        break
    print("Senha incorreta. Tente novamente.")
    print("Programa encerrado com sucesso.")'''

contador = 1 #variavel de inicio
while contador <= 5:
    print(contador)
    contador ==3