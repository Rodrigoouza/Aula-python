try:
    numero = int(input("Entre com a sua Idade: "))
    print(f"Você digitou a idade: {numero} ")
except ValueError:
    print("Erro: Por favor, digite um número inteiro válido.")  
else:
    print(f"Perfeito! Você digitou a idade {numero} e ela foi processada com sucesso.")
finally:
    print("Fim do programa. Obrigado por utilizar!")