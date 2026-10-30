"""
5) Escreva uma função que:
a) Receba uma frase como parâmetro.
b) Retorne uma nova frase com cada palavra com as letras invertidas.
"""

frase = 'eu amo voce'

def InverterPalavras(frase):
  palavras = frase.split(' ')
  for i in range(0, len(palavras)):
    palavras[i] = palavras[i][::-1]
  return " ".join(palavras)

fraseNova = InverterPalavras(frase)
print(fraseNova)