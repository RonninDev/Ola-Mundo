### 3 - Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma mensagem. Ex: Nome do Funcionário: Maria do Carmo Salário: 1850,45 O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho. ###

nome = input("Digite o Nome do Empregado:")
salario = float(input('Digite o Salário do Empregado: '))

print('Nome: ' + nome)
print('Salário: R$ ' + str(salario))
print('O Empregado(a) ' + nome + ' receberá R$ ' + str(salario) + ' no mês de Junho.')