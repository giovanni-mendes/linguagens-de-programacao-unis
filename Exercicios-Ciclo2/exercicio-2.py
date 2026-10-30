"""
2) Elaborar um programa que lê 3 valores a,b,c e verifica se eles formam ou
não um triângulo. Supor que os valores lidos são inteiros e positivos. Caso os
valores formem um triângulo, calcular e escrever a área deste triângulo. Se não
formam triângulo escrever os valores lidos. (Se a > b + c não formam triângulo
algum, se a é o maior).
"""
import math

ladosTriangulo = []

for i in range(0, 3):
  ladosTriangulo.append(int(input(f'Digite o {i + 1}° lado do triângulo: ')))

def VerificaTriangulo(listaLados):
  a, b, c = listaLados
  if a > b + c or b > a + c or c > a + b:
    print('Os seguintes lados inseridos não representam um triângulo.')
    for i in range(0, 3):
      print(f'Lado {i + 1}: {listaLados[i]} ')
    return 0
  else:
    return 1

def AreaTriangulo(listaLados):
  if VerificaTriangulo(listaLados):
    a, b, c = listaLados
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('A área do triângulo é: ', area)
    return area


AreaTriangulo(ladosTriangulo)