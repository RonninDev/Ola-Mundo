# Calcular Preço de um produto com o Imposto

""" preco = int(input('Qual o preço do produto: R$ '))
imposto = preco * 60/ 100
total = preco + imposto

print(preco)
print(imposto)
print(total)
 """
# Desafio - Qual o Valor do Empréstimo Juros de 20%, quantidades de parcelas e resultados
#       

emprestimo = int(input('Qual o valor desejo de Empréstimo? R$ '))
juros = emprestimo * 20/100
total = emprestimo + juros

print(f'A taxa de juros é de {juros}.')
print(f'O total a pagar é {total}')

parcelas = int(input('Em quantas parcelas você quer dividir esse valor? '))
if(parcelas > 24 or parcelas < 1):
    print("O número de parcelas deve ser entre 1 e 24x...")
else:
    print("Ok!")

calc = total / parcelas
print(calc)
print('')