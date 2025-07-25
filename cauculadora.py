import tkinter as tk
from tkinter import ttk

# Funções da calculadora
def clicar_botao(valor):
    entrada_atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, entrada_atual + str(valor))

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

def limpar():
    entrada.delete(0, tk.END)

# Interface da calculadora (em uma função para usar com __main__)
def iniciar_calculadora():
    global entrada
    janela = tk.Tk()
    janela.title("Calculadora Bonita")
    janela.geometry("320x450")
    janela.configure(bg="#f0f4f7")
    janela.resizable(False, False)

    # Estilo com ttk
    style = ttk.Style(janela)
    style.theme_use("clam")  # Tema mais moderno

    style.configure("TButton",
                    font=("Segoe UI", 16),
                    padding=10,
                    relief="flat",
                    background="#ffffff",
                    foreground="#333333")
    style.map("TButton",
              background=[("active", "#d9e2ec")])

    # Campo de entrada
    entrada = ttk.Entry(janela, font=("Segoe UI", 24), justify="right")
    entrada.pack(padx=15, pady=20, fill="x")

    # Grade de botões
    botoes = [
        ['7', '8', '9', '/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['0', '.', '=', '+']
    ]

    for linha in botoes:
        frame_linha = ttk.Frame(janela)
        frame_linha.pack(expand=True, fill="both", padx=10, pady=5)
        for botao in linha:
            if botao == '=':
                cmd = calcular
            else:
                cmd = lambda x=botao: clicar_botao(x)
            ttk.Button(frame_linha, text=botao, command=cmd).pack(side="left", expand=True, fill="both", padx=3, pady=3)

    # Botão limpar
    frame_limpar = ttk.Frame(janela)
    frame_limpar.pack(expand=True, fill="both", padx=10, pady=10)
    ttk.Button(frame_limpar, text="C", command=limpar).pack(side="left", expand=True, fill="both")

    janela.mainloop()

# Ponto de entrada
if __name__ == "__main__":
    iniciar_calculadora()

