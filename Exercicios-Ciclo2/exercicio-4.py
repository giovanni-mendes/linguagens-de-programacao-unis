"""
4) Implementar uma função que retorne verdadeiro se o número for primo
(falso caso contrário). Testar de 1 a 100.
"""

def verificaPrimo(numero):
  divisores = 0
  for i in range(1, numero + 1):
    if(numero % i == 0):
      divisores += 1

  if divisores == 2:
    return 1


listaPrimos = []

for numero in range(1, 101):
  if verificaPrimo(numero):
    listaPrimos.append(numero)

print(listaPrimos)