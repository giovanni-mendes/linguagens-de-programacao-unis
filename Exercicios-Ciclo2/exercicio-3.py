"""
3) Faça um programa que leia 3 números inteiros e mostre o menor deles.
"""

numeros = []

for i in range(0, 3):
  numeros.append(int(input(f'Digite o {i + 1}° número: ')))

numeros.sort()

print('O menor número entre os inseridos é o: ', numeros[0])