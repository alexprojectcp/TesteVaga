c = 1
numeros = list()
n = int(input("Digite um número inteiro de 1 à 1000: "))
if n < 1 or n > 1000:
    print("Número inválido! Digite um número inteiro de 1 à 1000 ")
else:
    print("Digite {} números inteiros de -1000 à 1000:".format(n))
    for c in range(n):
      k = int(input())
      if k not in numeros:
        numeros.append(k)

numeros.sort()
print(numeros)

