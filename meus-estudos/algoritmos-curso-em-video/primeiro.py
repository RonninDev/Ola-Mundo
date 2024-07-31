print("Olá, Mundo!")
print("Me livrei da maldição") 

print("O seu primeiro algoritmo é me dar seu nome.")
nome = input("Digite seu Nome:")
print("Olá, " + nome + "!")



print("Crie um Algoritmo que leia os lados de um triângulo e diga se ele é Equilátero ou Escaleno")

l1 = int(input('Digite o primeiro lado: '))
l2 = int(input('Digite o segundo lado: '))
l3 = int(input('Digite o terceiro lado: '))

tringulo = (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2)
equilatero = (l1 == l2) and (l2 == l3)
escaleno = (l1 != l2) and (l2 != l3) and (l1 != l3)

print(equilatero)
print(escaleno)

