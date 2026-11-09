import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()

janela.title('Cálculo do IMC - índice de Massa Corporal')
janela.geometry('500x300')
janela.resizable(False, False)

# Configurações do Grid
framePrincipal = tk.Frame(janela)
framePrincipal.pack(fill="both", expand=True, padx=10, pady=10)
framePrincipal.grid_columnconfigure(0, minsize=130)
framePrincipal.grid_columnconfigure(1, minsize=155)

# Paciente
tk.Label(framePrincipal,
        text='Nome do Paciente:', 
        width=15, 
        anchor='w').grid(row=0, column=0, pady=(20,10), sticky='w')

entradaNome = tk.Entry(framePrincipal, width=65)
entradaNome.grid(row=0, column=1, columnspan=2, pady=(20,10), sticky='w')

# Endereço
tk.Label(framePrincipal,
        text='Endereço Completo:', 
        width=15, 
        anchor='w').grid(row=1, column=0, pady=5, sticky='w')

entradaEndereço = tk.Entry(framePrincipal, width=65)
entradaEndereço.grid(row=1, column=1, columnspan=2, pady=5, sticky='w')

# Altura
tk.Label(framePrincipal,
        text='Altura (cm):', 
        width=15, 
        anchor='w').grid(row=2, column=0, pady=5, sticky='w')

entradaAltura = tk.Entry(framePrincipal, width=15)
entradaAltura.grid(row=2, column=1, columnspan=2, pady=5, sticky='w')

# Peso
tk.Label(framePrincipal,
        text='Peso (kg):', 
        width=15, 
        anchor='w').grid(row=3, column=0, pady=5, sticky='w')

entradaPeso = tk.Entry(framePrincipal, width=15)
entradaPeso.grid(row=3, column=1, columnspan=2, pady=5, sticky='w')

# JanelaResultado

resultado = tk.Label(
    janela,
    text="Aguardando cálculo",
    relief="solid",
    borderwidth=1,
    width=25,
    height=7,
    font=("Arial", 12)
)
resultado.place(x=250, y=95)

# Funções

def imc():
  try:
    alturaFormatada = float(entradaAltura.get().replace(',', '.')) / 100
    peso = float(entradaPeso.get().replace(',', '.'))

    if not alturaFormatada or alturaFormatada < 0 or not peso or peso < 0:
      raise ValueError

    imc = peso / (alturaFormatada ** 2)

    classificacaoImc = ''
    if imc < 18.5:
      classificacaoImc = 'Abaixo do peso normal'
    elif imc <= 24.9:
      classificacaoImc = 'Peso normal'
    elif imc <= 29.9:
          classificacaoImc = 'Excesso de Peso'
    elif imc <= 34.9:
          classificacaoImc = 'Obesidade classe I'
    elif imc <= 39.9:
              classificacaoImc = 'Obesidade classe II'
    else:
        classificacaoImc = 'Obesidade classe III'

    resultado.config(
      text=f"Paciente: {entradaNome.get()}\n\nIMC: {imc:.2f} kg/m²\n\n {classificacaoImc}"
    )

  except ValueError:
    messagebox.showerror('Erro', 'Informe valores válidos para altura e peso.')

def reiniciar():
  entradaNome.delete(0, tk.END)
  entradaEndereço.delete(0, tk.END)
  entradaAltura.delete(0, tk.END)
  entradaPeso.delete(0, tk.END)
  resultado.config(text="Aguardando cálculo")

# Botão calcular IMC

tk.Button(
    janela,
    text="Calcular",
    width=12,
    command=imc,
).place(x=130, y=240)

# Botão reiniciar dados

tk.Button(
    janela,
    text="Reiniciar",
    width=12,
    command=reiniciar
).place(x=230, y=240)

# Botão sair

tk.Button(
    janela,
    text="Sair",
    width=12,
    command=janela.destroy
).place(x=385, y=240)

janela.mainloop()