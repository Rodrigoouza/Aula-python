'''Quant_Funcionarios = int (input ('Digite o numero de funcionarios: '))
Quant_Canetas= int (input ('Digite o numero de canetas: ')) 
soma = Quant_Funcionarios // Quant_Canetas
print(f'Cada funcionario ganhara {soma}')'''

#"atividae 2"
 
'''doces_produzidos = int (input ("Quantos doces foram produzidos?"))
soma = doces_produzidos % 6
print (f'quantidade de doces que sobra: {soma}')'''

# atividade 3
'''coletados = int (input ("Quantos critais foram coletados?"))
caixotes = int (input ("Quantas cristais por caixa?"))
caixas_usadas = coletados // caixotes
sobra = coletados % caixotes
consumo = coletados ** 2  

print (f'quantidade de caixas de critais: {caixas_usadas}')
print (f"quantidade de critais que nao foram alocados: {sobra}")
print (f'consumo de energia: {consumo}')'''

# atividade 4
'''vendas_pri = int (input ("Quantas vendas foram realizadas na primeira quinzena?"))
vendas_seg = int (input ("Quantas vendas foram realizadas na segunda quinzena?"))
total_vendas = vendas_pri + vendas_seg
if total_vendas >= 50:
    print (f'Você atingiu a meta de: {total_vendas}')
else:
    print (f'Você não atingiu a meta. Total de vendas: {total_vendas}')'''

# atividade 5
'''compra = int (input ("Qual o valor total da compra?"))
if compra >= 150:
    desconto = compra * 0.1
    soma = compra - desconto
    print (f'Você tem direito a um desconto de 10% na compra.')
    print (f'Valor do desconto: {desconto}')
    print (f'Valor total com desconto: {soma}')
else:
    print (f'Você não tem direito a um desconto na compra.')'''

# atividade 6
'''nota_1 = float (input ("Digite a primeira nota: "))
nota_2 = float (input ("Digite a segunda nota: "))
media = (nota_1 + nota_2) / 2

if media >= 6:
    print (f'Você foi aprovado com média: {media}')
else:
    print (f'Você foi reprovado com média: {media}')'''

# atividade 7
"""nota_1 = float (input ("Digite a primeira nota: "))
nota_2 = float (input ("Digite a segunda nota: "))
media = (nota_1 + nota_2) / 2
if nota_1 <= 10 and nota_2 <= 10:
    if media >= 6:
        print (f'Você foi aprovado com média: {media}')
    else:
        print (f'Você foi reprovado com média: {media}')
else:
    print (f'Notas inválidas. Por favor, digite notas entre 0 e 10.')"""

# atividade 8

"""velocidade = int (input ("Digite a velocidade do veículo: "))
if velocidade >= 80:
    multa = (velocidade - 80) * 7
    print (f'Você está acima da velocidade permitida: {velocidade} km/h')
    print (f'Valor da multa: R$ {multa:.2f}')
else:
    print (f'Você está na velocidade permitida: {velocidade} km/h')"""

# atividade 9
'''estado_civil = str(input ('Digite o estado civil (casado/solteiro/divorciado/noivo/viuvo/namorando): '))
if estado_civil == "casado":
    print("Você está casado.")
elif estado_civil == "solteiro":
    print("Você está solteiro.")
elif estado_civil == "divorciado":
    print("Você está divorciado.")
elif estado_civil == "noivo":
    print("Você está noivo.")
elif estado_civil == "viuvo":
    print("Você está viúvo.")
elif estado_civil == "namorando":
    print("Você está namorando.")
else:
    print("Estado civil inválido.")'''

# atividade 8
"""lixo = str(input("Digite o seu Material do seu lixo: "))
 
if lixo == "papel":
    print("Direcionado para lixeira AZUL.")
elif lixo == "plástico":
    print("Direcionado para lixeira VERMELHA.")
elif lixo == "vidro":
    print("Direcionado para lixeira VERDE.")
elif lixo == "metal":
    print("Direcionado para lixeira AMARELA.")
elif lixo == "orgânico":
    print("Direcionado para lixeira CINZA.")    
else:
    print("Material de lixo inválido. Por favor, digite um material válido.")"""

# atividade 9
"""estacionamento = int(input("Digite vagas do estacionamento: "))
if estacionamento == 100:
    print("O estacionamento está cheio.")
elif estacionamento < 100:
    print(f"O estacionamento ainda tem vagas {100 - estacionamento} disponíveis.")

else:
    print("Número de vagas inválido digite um número entre 0 e 100.")"""

# atividade 10
"""pontuacao = int(input("Digite a pontuação da caldeira: "))
if pontuacao <= 0:
    print("pontuação invalida coloque um valor entre 1 e 10.")
elif pontuacao <= 3:
    print("Alerta Baixo da caldeira.")
elif pontuacao <= 7:
    print("Alerta Médio da caldeira.")
elif pontuacao <= 10:
    print("Alerta Alto da caldeira.")
else:
    print("pontuação invalida coloque um valor entre 1 e 10.")"""