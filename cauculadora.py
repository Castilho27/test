import tkinter as tk

# Função para atualizar o texto no display
def clicar_botao(valor):
    entrada_atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, entrada_atual + str(valor))

# Função para calcular o resultado
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

# Função para limpar o display
def limpar():
    entrada.delete(0, tk.END)

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.resizable(False, False)

# Campo de entrada
entrada = tk.Entry(janela, font=("Arial", 24), borderwidth=5, relief="ridge", justify="right")
entrada.pack(pady=20, padx=10, fill='x')

# Grade de botões
botoes = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Criando os botões
for linha in botoes:
    frame_linha = tk.Frame(janela)
    frame_linha.pack(expand=True, fill="both")
    for botao in linha:
        if botao == '=':
            cmd = calcular
        else:
            cmd = lambda x=botao: clicar_botao(x)
        tk.Button(frame_linha, text=botao, font=("Arial", 18), command=cmd, height=2, width=5).pack(side="left", expand=True, fill="both")

# Botão de limpar
botao_limpar = tk.Button(janela, text="C", font=("Arial", 18), command=limpar, bg="#f44336", fg="white", height=2)
botao_limpar.pack(expand=True, fill="both", padx=10, pady=10)

# Iniciar o loop da interface
janela.mainloop()

