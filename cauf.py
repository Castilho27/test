import tkinter as tk
from tkinter import messagebox

# --- Classe para a lógica da fração ---
class Fracao:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("O denominador não pode ser zero.")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar() # Simplifica a fração assim que ela é criada

    def __str__(self):
        # Representação da fração como string (ex: "1/2")
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, outra):
        # Soma de frações
        novo_numerador = (self.numerador * outra.denominador) + \
                         (outra.numerador * self.denominador)
        novo_denominador = self.denominador * outra.denominador
        return Fracao(novo_numerador, novo_denominador)

    def __sub__(self, outra):
        # Subtração de frações
        novo_numerador = (self.numerador * outra.denominador) - \
                         (outra.numerador * self.denominador)
        novo_denominador = self.denominador * outra.denominador
        return Fracao(novo_numerador, novo_denominador)

    def __mul__(self, outra):
        # Multiplicação de frações
        novo_numerador = self.numerador * outra.numerador
        novo_denominador = self.denominador * outra.denominador
        return Fracao(novo_numerador, novo_denominador)

    def __truediv__(self, outra):
        # Divisão de frações (multiplica pela inversa)
        if outra.numerador == 0:
            raise ValueError("Não é possível dividir por uma fração zero.")
        novo_numerador = self.numerador * outra.denominador
        novo_denominador = self.denominador * outra.numerador
        return Fracao(novo_numerador, novo_denominador)

    def mdc(self, a, b):
        # Máximo Divisor Comum (usado para simplificar)
        while b:
            a, b = b, a % b
        return a

    def simplificar(self):
        # Simplifica a fração dividindo numerador e denominador pelo MDC
        divisor = self.mdc(abs(self.numerador), abs(self.denominador))
        self.numerador //= divisor
        self.denominador //= divisor
        # Garante que o sinal esteja no numerador, se houver
        if self.denominador < 0:
            self.numerador *= -1
            self.denominador *= -1

# --- Interface Gráfica com Tkinter ---
class CalculadoraFracao:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Frações")

        # --- Frames para organizar a UI ---
        self.frame_fracao1 = tk.Frame(master, padx=10, pady=5)
        self.frame_fracao1.pack()

        self.frame_operacao = tk.Frame(master, padx=10, pady=5)
        self.frame_operacao.pack()

        self.frame_fracao2 = tk.Frame(master, padx=10, pady=5)
        self.frame_fracao2.pack()

        self.frame_botoes = tk.Frame(master, padx=10, pady=5)
        self.frame_botoes.pack()

        self.frame_resultado = tk.Frame(master, padx=10, pady=5)
        self.frame_resultado.pack()

        # --- Fracão 1 ---
        tk.Label(self.frame_fracao1, text="Fração 1:").pack(side=tk.LEFT)
        self.num1_entry = tk.Entry(self.frame_fracao1, width=5)
        self.num1_entry.pack(side=tk.LEFT)
        tk.Label(self.frame_fracao1, text="/").pack(side=tk.LEFT)
        self.den1_entry = tk.Entry(self.frame_fracao1, width=5)
        self.den1_entry.pack(side=tk.LEFT)

        # --- Operação ---
        tk.Label(self.frame_operacao, text="Operação:").pack(side=tk.LEFT)
        self.operacao_var = tk.StringVar(master)
        self.operacao_var.set("+") # Valor padrão
        self.operacao_menu = tk.OptionMenu(self.frame_operacao, self.operacao_var, "+", "-", "*", "/")
        self.operacao_menu.pack(side=tk.LEFT)

        # --- Fracão 2 ---
        tk.Label(self.frame_fracao2, text="Fração 2:").pack(side=tk.LEFT)
        self.num2_entry = tk.Entry(self.frame_fracao2, width=5)
        self.num2_entry.pack(side=tk.LEFT)
        tk.Label(self.frame_fracao2, text="/").pack(side=tk.LEFT)
        self.den2_entry = tk.Entry(self.frame_fracao2, width=5)
        self.den2_entry.pack(side=tk.LEFT)

        # --- Botão Calcular ---
        self.calcular_button = tk.Button(self.frame_botoes, text="Calcular", command=self.calcular)
        self.calcular_button.pack()

        # --- Resultado ---
        tk.Label(self.frame_resultado, text="Resultado:").pack(side=tk.LEFT)
        self.resultado_label = tk.Label(self.frame_resultado, text="Aguardando...")
        self.resultado_label.pack(side=tk.LEFT)

    def obter_fracao(self, num_entry, den_entry):
        try:
            numerador = int(num_entry.get())
            denominador = int(den_entry.get())
            return Fracao(numerador, denominador)
        except ValueError as e:
            messagebox.showerror("Erro de Entrada", f"Entrada inválida. Certifique-se de digitar números inteiros. {e}")
            return None

    def calcular(self):
        fracao1 = self.obter_fracao(self.num1_entry, self.den1_entry)
        fracao2 = self.obter_fracao(self.num2_entry, self.den2_entry)

        if fracao1 is None or fracao2 is None:
            return

        operacao = self.operacao_var.get()
        resultado = None

        try:
            if operacao == "+":
                resultado = fracao1 + fracao2
            elif operacao == "-":
                resultado = fracao1 - fracao2
            elif operacao == "*":
                resultado = fracao1 * fracao2
            elif operacao == "/":
                resultado = fracao1 / fracao2
            else:
                messagebox.showerror("Erro", "Operação inválida.")
                return

            self.resultado_label.config(text=str(resultado))
        except ValueError as e:
            messagebox.showerror("Erro de Cálculo", str(e))
        except Exception as e:
            messagebox.showerror("Erro Inesperado", f"Ocorreu um erro: {e}")

# --- Executa a aplicação ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraFracao(root)
    root.mainloop()