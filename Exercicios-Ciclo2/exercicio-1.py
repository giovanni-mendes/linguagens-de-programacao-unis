# 1) Faça um programa que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.

idadeDias = int(input('Digite a sua idade: '))

def calculadoraIdade(idade):
  anos = idade // 365
  meses = (idade % 365) // 30
  dias = (idade % 365) % 30
  print(f"Você tem {anos} anos, {meses} meses e {dias} dias de idade!")

calculadoraIdade(idadeDias)