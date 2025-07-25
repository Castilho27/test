import tkinter as tk
from tkinter import ttk

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

def iniciar_calculadora():
    global entrada
    janela = tk.Tk()
    janela.title("Calculadora Dark Bonita")
    janela.geometry("320x500")
    janela.configure(bg="#1e1e1e")
    janela.resizable(False, False)

    # Campo de entrada com estilo visor verde
    entrada = tk.Entry(janela, font=("Courier New", 24), justify="right",
                       bg="#003300", fg="#00FF00", insertbackground="#00FF00",
                       relief="flat", bd=10)
    entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

    # Botões
    botoes = [
        ['7', '8', '9', '/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['0', '.', '=', '+']
    ]

    estilo_botao = {
        "font": ("Segoe UI", 16),
        "bg": "#2d2d2d",
        "fg": "#ffffff",
        "activebackground": "#444444",
        "activeforeground": "#00ffcc",
        "relief": "flat",
        "bd": 0
    }

    for i, linha in enumerate(botoes):
        for j, texto in enumerate(linha):
            if texto == '=':
                cmd = calcular
            else:
                cmd = lambda x=texto: clicar_botao(x)
            tk.Button(janela, text=texto, command=cmd, **estilo_botao).grid(
                row=i + 1, column=j, padx=5, pady=5, sticky="nsew"
            )

    # Botão limpar (linha separada, ocupa 4 colunas)
    tk.Button(janela, text="C", command=limpar, **estilo_botao).grid(
        row=5, column=0, columnspan=4, padx=10, pady=15, sticky="nsew"
    )

    # Ajuste das proporções
    for i in range(6):
        janela.rowconfigure(i, weight=1)
    for j in range(4):
        janela.columnconfigure(j, weight=1)

    janela.mainloop()

if __name__ == "__main__":
    iniciar_calculadora()



