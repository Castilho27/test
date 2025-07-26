import tkinter as tk
from tkinter import messagebox
import math # Para math.gcd

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

    def __lt__(self, outra):
        # Comparação: menor que (<)
        return (self.numerador * outra.denominador) < (outra.numerador * self.denominador)

    def __le__(self, outra):
        # Comparação: menor ou igual (<=)
        return (self.numerador * outra.denominador) <= (outra.numerador * self.denominador)

    def __eq__(self, outra):
        # Comparação: igual (==)
        return (self.numerador * outra.denominador) == (outra.numerador * self.denominador)

    def __ne__(self, outra):
        # Comparação: diferente (!=)
        return not self.__eq__(outra)

    def __gt__(self, outra):
        # Comparação: maior que (>)
        return (self.numerador * outra.denominador) > (outra.numerador * self.denominador)

    def __ge__(self, outra):
        # Comparação: maior ou igual (>=)
        return (self.numerador * outra.denominador) >= (outra.numerador * self.denominador)

    def mdc(self, a, b):
        # Máximo Divisor Comum (usado para simplificar)
        return math.gcd(a, b) # Usando math.gcd do Python 3.5+

    def simplificar(self):
        # Simplifica a fração dividindo numerador e denominador pelo MDC
        divisor = self.mdc(abs(self.numerador), abs(self.denominador))
        self.numerador //= divisor
        self.denominador //= divisor
        # Garante que o sinal esteja no numerador, se houver
        if self.denominador < 0:
            self.numerador *= -1
            self.denominador *= -1

    def para_misto(self):
        # Converte fração imprópria para número misto
        if abs(self.numerador) < self.denominador:
            return str(self) # Já é uma fração própria
        
        parte_inteira = self.numerador // self.denominador
        resto_numerador = abs(self.numerador) % self.denominador
        
        if resto_numerador == 0:
            return str(parte_inteira)
        
        # Garante o sinal correto para a parte fracionária
        if self.numerador < 0 and parte_inteira == 0:
            return f"-{abs(resto_numerador)}/{self.denominador}"
        elif self.numerador < 0:
             return f"{parte_inteira} {abs(resto_numerador)}/{self.denominador}"
        else:
             return f"{parte_inteira} {resto_numerador}/{self.denominador}"


    @staticmethod
    def de_misto(inteiro_str, numerador_str, denominador_str):
        # Converte strings de número misto para um objeto Fracao
        try:
            inteiro = int(inteiro_str) if inteiro_str else 0
            numerador = int(numerador_str)
            denominador = int(denominador_str)

            if denominador == 0:
                raise ValueError("O denominador não pode ser zero.")

            if inteiro < 0:
                numerador = inteiro * denominador - numerador
            else:
                numerador = inteiro * denominador + numerador
            
            return Fracao(numerador, denominador)
        except ValueError as e:
            raise ValueError(f"Entrada inválida para número misto: {e}")

# --- Interface Gráfica com Tkinter ---
class CalculadoraFracao:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Frações")
        master.geometry("400x450") # Tamanho inicial da janela

        self.frames = {} # Dicionário para armazenar os frames de cada opção
        self.criar_menu_principal()
        self.criar_frames_operacoes()

        self.mostrar_frame("menu_principal")

    def criar_menu_principal(self):
        menu_frame = tk.Frame(self.master, padx=20, pady=20)
        self.frames["menu_principal"] = menu_frame

        tk.Label(menu_frame, text="Escolha uma operação:", font=("Arial", 14, "bold")).pack(pady=10)

        opcoes = [
            ("Simplificar", "simplificar"),
            ("Soma, subtração, multiplicação e divisão", "aritmetica"),
            ("Comparação", "comparacao"),
            ("Números mistos e frações impróprias", "mistos_improprias")
        ]

        for texto, comando in opcoes:
            tk.Button(menu_frame, text=texto, command=lambda c=comando: self.mostrar_frame(c),
                      font=("Arial", 12), width=35, height=2).pack(pady=5)
    
    def criar_frames_operacoes(self):
        # --- Frame de Aritmética (Soma, Subtração, Multiplicação, Divisão) ---
        aritmetica_frame = tk.Frame(self.master, padx=10, pady=10)
        self.frames["aritmetica"] = aritmetica_frame

        tk.Label(aritmetica_frame, text="Operações Aritméticas", font=("Arial", 14, "bold")).pack(pady=5)

        # Fracão 1
        frame_f1 = tk.Frame(aritmetica_frame)
        frame_f1.pack(pady=5)
        tk.Label(frame_f1, text="Fração 1:").pack(side=tk.LEFT)
        self.num1_entry = tk.Entry(frame_f1, width=7)
        self.num1_entry.pack(side=tk.LEFT)
        tk.Label(frame_f1, text="/").pack(side=tk.LEFT)
        self.den1_entry = tk.Entry(frame_f1, width=7)
        self.den1_entry.pack(side=tk.LEFT)

        # Operação
        frame_op = tk.Frame(aritmetica_frame)
        frame_op.pack(pady=5)
        tk.Label(frame_op, text="Operação:").pack(side=tk.LEFT)
        self.operacao_var = tk.StringVar(self.master)
        self.operacao_var.set("+")
        self.operacao_menu = tk.OptionMenu(frame_op, self.operacao_var, "+", "-", "*", "/")
        self.operacao_menu.pack(side=tk.LEFT)

        # Fracão 2
        frame_f2 = tk.Frame(aritmetica_frame)
        frame_f2.pack(pady=5)
        tk.Label(frame_f2, text="Fração 2:").pack(side=tk.LEFT)
        self.num2_entry = tk.Entry(frame_f2, width=7)
        self.num2_entry.pack(side=tk.LEFT)
        tk.Label(frame_f2, text="/").pack(side=tk.LEFT)
        self.den2_entry = tk.Entry(frame_f2, width=7)
        self.den2_entry.pack(side=tk.LEFT)

        tk.Button(aritmetica_frame, text="Calcular", command=self.calcular_aritmetica).pack(pady=10)
        tk.Label(aritmetica_frame, text="Resultado:").pack()
        self.resultado_aritmetica_label = tk.Label(aritmetica_frame, text="Aguardando...", font=("Arial", 12))
        self.resultado_aritmetica_label.pack()
        tk.Button(aritmetica_frame, text="Voltar ao Menu", command=lambda: self.mostrar_frame("menu_principal")).pack(pady=10)

        # --- Frame de Simplificar ---
        simplificar_frame = tk.Frame(self.master, padx=10, pady=10)
        self.frames["simplificar"] = simplificar_frame

        tk.Label(simplificar_frame, text="Simplificar Fração", font=("Arial", 14, "bold")).pack(pady=5)
        
        frame_simples = tk.Frame(simplificar_frame)
        frame_simples.pack(pady=5)
        tk.Label(frame_simples, text="Fração:").pack(side=tk.LEFT)
        self.num_simples_entry = tk.Entry(frame_simples, width=7)
        self.num_simples_entry.pack(side=tk.LEFT)
        tk.Label(frame_simples, text="/").pack(side=tk.LEFT)
        self.den_simples_entry = tk.Entry(frame_simples, width=7)
        self.den_simples_entry.pack(side=tk.LEFT)

        tk.Button(simplificar_frame, text="Simplificar", command=self.calcular_simplificar).pack(pady=10)
        tk.Label(simplificar_frame, text="Fração Simplificada:").pack()
        self.resultado_simplificar_label = tk.Label(simplificar_frame, text="Aguardando...", font=("Arial", 12))
        self.resultado_simplificar_label.pack()
        tk.Button(simplificar_frame, text="Voltar ao Menu", command=lambda: self.mostrar_frame("menu_principal")).pack(pady=10)

        # --- Frame de Comparação ---
        comparacao_frame = tk.Frame(self.master, padx=10, pady=10)
        self.frames["comparacao"] = comparacao_frame

        tk.Label(comparacao_frame, text="Comparar Frações", font=("Arial", 14, "bold")).pack(pady=5)
        
        # Fracão 1
        frame_comp1 = tk.Frame(comparacao_frame)
        frame_comp1.pack(pady=5)
        tk.Label(frame_comp1, text="Fração 1:").pack(side=tk.LEFT)
        self.num_comp1_entry = tk.Entry(frame_comp1, width=7)
        self.num_comp1_entry.pack(side=tk.LEFT)
        tk.Label(frame_comp1, text="/").pack(side=tk.LEFT)
        self.den_comp1_entry = tk.Entry(frame_comp1, width=7)
        self.den_comp1_entry.pack(side=tk.LEFT)

        # Fracão 2
        frame_comp2 = tk.Frame(comparacao_frame)
        frame_comp2.pack(pady=5)
        tk.Label(frame_comp2, text="Fração 2:").pack(side=tk.LEFT)
        self.num_comp2_entry = tk.Entry(frame_comp2, width=7)
        self.num_comp2_entry.pack(side=tk.LEFT)
        tk.Label(frame_comp2, text="/").pack(side=tk.LEFT)
        self.den_comp2_entry = tk.Entry(frame_comp2, width=7)
        self.den_comp2_entry.pack(side=tk.LEFT)

        tk.Button(comparacao_frame, text="Comparar", command=self.calcular_comparacao).pack(pady=10)
        tk.Label(comparacao_frame, text="Resultado da Comparação:").pack()
        self.resultado_comparacao_label = tk.Label(comparacao_frame, text="Aguardando...", font=("Arial", 12))
        self.resultado_comparacao_label.pack()
        tk.Button(comparacao_frame, text="Voltar ao Menu", command=lambda: self.mostrar_frame("menu_principal")).pack(pady=10)

        # --- Frame de Números Mistos e Frações Impróprias ---
        mistos_improprias_frame = tk.Frame(self.master, padx=10, pady=10)
        self.frames["mistos_improprias"] = mistos_improprias_frame

        tk.Label(mistos_improprias_frame, text="Números Mistos e Frações Impróprias", font=("Arial", 14, "bold")).pack(pady=5)

        # Conversão de Imprópria para Mista
        tk.Label(mistos_improprias_frame, text="Fração Imprópria para Mista:").pack(pady=(10, 0))
        frame_imp_to_mist = tk.Frame(mistos_improprias_frame)
        frame_imp_to_mist.pack(pady=5)
        tk.Label(frame_imp_to_mist, text="Numerador:").pack(side=tk.LEFT)
        self.num_imp_entry = tk.Entry(frame_imp_to_mist, width=7)
        self.num_imp_entry.pack(side=tk.LEFT)
        tk.Label(frame_imp_to_mist, text="Denominador:").pack(side=tk.LEFT)
        self.den_imp_entry = tk.Entry(frame_imp_to_mist, width=7)
        self.den_imp_entry.pack(side=tk.LEFT)
        tk.Button(mistos_improprias_frame, text="Converter para Misto", command=self.converter_impropria_para_mista).pack(pady=5)
        self.resultado_imp_to_mist_label = tk.Label(mistos_improprias_frame, text="Aguardando...", font=("Arial", 12))
        self.resultado_imp_to_mist_label.pack()

        # Conversão de Mista para Imprópria
        tk.Label(mistos_improprias_frame, text="Número Misto para Fração Imprópria:").pack(pady=(10, 0))
        frame_mist_to_imp = tk.Frame(mistos_improprias_frame)
        frame_mist_to_imp.pack(pady=5)
        tk.Label(frame_mist_to_imp, text="Inteiro:").pack(side=tk.LEFT)
        self.inteiro_misto_entry = tk.Entry(frame_mist_to_imp, width=5)
        self.inteiro_misto_entry.pack(side=tk.LEFT)
        tk.Label(frame_mist_to_imp, text="Numerador:").pack(side=tk.LEFT)
        self.num_misto_entry = tk.Entry(frame_mist_to_imp, width=5)
        self.num_misto_entry.pack(side=tk.LEFT)
        tk.Label(frame_mist_to_imp, text="/").pack(side=tk.LEFT)
        self.den_misto_entry = tk.Entry(frame_mist_to_imp, width=5)
        self.den_misto_entry.pack(side=tk.LEFT)
        tk.Button(mistos_improprias_frame, text="Converter para Imprópria", command=self.converter_mista_para_impropria).pack(pady=5)
        self.resultado_mist_to_imp_label = tk.Label(mistos_improprias_frame, text="Aguardando...", font=("Arial", 12))
        self.resultado_mist_to_imp_label.pack()

        tk.Button(mistos_improprias_frame, text="Voltar ao Menu", command=lambda: self.mostrar_frame("menu_principal")).pack(pady=10)


    def mostrar_frame(self, nome_frame):
        # Esconde todos os frames e mostra apenas o selecionado
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[nome_frame].pack(fill="both", expand=True)

    def obter_fracao(self, num_entry, den_entry):
        try:
            numerador = int(num_entry.get())
            denominador = int(den_entry.get())
            return Fracao(numerador, denominador)
        except ValueError as e:
            messagebox.showerror("Erro de Entrada", f"Entrada inválida. Certifique-se de digitar números inteiros. Detalhe: {e}")
            return None

    def calcular_aritmetica(self):
        fracao1 = self.obter_fracao(self.num1_entry, self.den1_entry)
        fracao2 = self.obter_fracao(self.num2_entry, self.den2_entry)

        if fracao1 is None or fracao2 is None:
            self.resultado_aritmetica_label.config(text="Erro na entrada.")
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

            self.resultado_aritmetica_label.config(text=str(resultado))
        except ValueError as e:
            messagebox.showerror("Erro de Cálculo", str(e))
            self.resultado_aritmetica_label.config(text="Erro no cálculo.")
        except Exception as e:
            messagebox.showerror("Erro Inesperado", f"Ocorreu um erro: {e}")
            self.resultado_aritmetica_label.config(text="Erro inesperado.")

    def calcular_simplificar(self):
        try:
            fracao_original = self.obter_fracao(self.num_simples_entry, self.den_simples_entry)
            if fracao_original:
                # A simplificação já ocorre no construtor da Fracao
                self.resultado_simplificar_label.config(text=str(fracao_original))
        except Exception as e:
            messagebox.showerror("Erro de Simplificação", str(e))
            self.resultado_simplificar_label.config(text="Erro na simplificação.")

    def calcular_comparacao(self):
        fracao1 = self.obter_fracao(self.num_comp1_entry, self.den_comp1_entry)
        fracao2 = self.obter_fracao(self.num_comp2_entry, self.den_comp2_entry)

        if fracao1 is None or fracao2 is None:
            self.resultado_comparacao_label.config(text="Erro na entrada.")
            return
        
        resultado_texto = ""
        if fracao1 < fracao2:
            resultado_texto = f"{fracao1} é MENOR que {fracao2}"
        elif fracao1 > fracao2:
            resultado_texto = f"{fracao1} é MAIOR que {fracao2}"
        else:
            resultado_texto = f"{fracao1} é IGUAL a {fracao2}"
        
        self.resultado_comparacao_label.config(text=resultado_texto)

    def converter_impropria_para_mista(self):
        try:
            fracao_impropria = self.obter_fracao(self.num_imp_entry, self.den_imp_entry)
            if fracao_impropria:
                self.resultado_imp_to_mist_label.config(text=fracao_impropria.para_misto())
        except Exception as e:
            messagebox.showerror("Erro de Conversão", str(e))
            self.resultado_imp_to_mist_label.config(text="Erro na conversão.")

    def converter_mista_para_impropria(self):
        try:
            # Pegar os valores de inteiro, numerador e denominador
            inteiro_str = self.inteiro_misto_entry.get()
            numerador_str = self.num_misto_entry.get()
            denominador_str = self.den_misto_entry.get()

            fracao_impropria = Fracao.de_misto(inteiro_str, numerador_str, denominador_str)
            self.resultado_mist_to_imp_label.config(text=str(fracao_impropria))
        except ValueError as e:
            messagebox.showerror("Erro de Entrada", str(e))
            self.resultado_mist_to_imp_label.config(text="Erro na entrada.")
        except Exception as e:
            messagebox.showerror("Erro de Conversão", str(e))
            self.resultado_mist_to_imp_label.config(text="Erro na conversão.")

# --- Executa a aplicação ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraFracao(root)
    root.mainloop()