import tkinter as tk
from tkinter import messagebox
import math 

# --- Classe para a lógica da fração ---
class Fracao:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("O denominador não pode ser zero.")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar() 

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, outra):
        novo_numerador = (self.numerador * outra.denominador) + \
                         (outra.numerador * self.denominador)
        novo_denominador = self.denominador * outra.denominador
        return Fracao(novo_numerador, novo_denominador)

    def __sub__(self, outra):
        novo_numerador = (self.numerador * outra.denominador) - \
                         (outra.numerador * self.denominador)
        novo_denominador = self.denominador * outra.denominador
        return Fracao(novo_numerador, novo_denominador)

    def __mul__(self, outra):
        novo_numerador = self.numerador * outra.numerador
        novo_denominador = self.denominador * outra.denominador
        return Fracao(novo_numerador, novo_denominador)

    def __truediv__(self, outra):
        if outra.numerador == 0:
            raise ValueError("Não é possível dividir por uma fração zero.")
        novo_numerador = self.numerador * outra.denominador
        novo_denominador = self.denominador * outra.numerador
        return Fracao(novo_numerador, novo_denominador)

    def __lt__(self, outra):
        return (self.numerador * outra.denominador) < (outra.numerador * self.denominador)

    def __le__(self, outra):
        return (self.numerador * outra.denominador) <= (outra.numerador * self.denominador)

    def __eq__(self, outra):
        return (self.numerador * outra.denominador) == (outra.numerador * self.denominador)

    def __ne__(self, outra):
        return not self.__eq__(outra)

    def __gt__(self, outra):
        return (self.numerador * outra.denominador) > (outra.numerador * self.denominador)

    def __ge__(self, outra):
        return (self.numerador * outra.denominador) >= (outra.numerador * self.denominador)

    def mdc(self, a, b):
        return math.gcd(a, b) 

    def simplificar(self):
        divisor = self.mdc(abs(self.numerador), abs(self.denominador))
        self.numerador //= divisor
        self.denominador //= divisor
        if self.denominador < 0:
            self.numerador *= -1
            self.denominador *= -1

    def para_misto(self):
        if abs(self.numerador) < self.denominador:
            return str(self) 
        
        parte_inteira = self.numerador // self.denominador
        resto_numerador = abs(self.numerador) % self.denominador
        
        if resto_numerador == 0:
            return str(parte_inteira)
        
        if self.numerador < 0 and parte_inteira == 0:
            return f"-{abs(resto_numerador)}/{self.denominador}"
        elif self.numerador < 0:
             return f"{parte_inteira} {abs(resto_numerador)}/{self.denominador}"
        else:
             return f"{parte_inteira} {resto_numerador}/{self.denominador}"


    @staticmethod
    def de_misto(inteiro_str, numerador_str, denominador_str):
        try:
            inteiro = int(inteiro_str) if inteiro_str else 0
            numerador = int(numerador_str)
            denominador = int(denominador_str)

            if denominador == 0:
                raise ValueError("O denominador não pode ser zero.")

            if inteiro < 0: # Lida com o sinal da parte inteira
                numerador_total = inteiro * denominador - numerador
            else:
                numerador_total = inteiro * denominador + numerador
            
            return Fracao(numerador_total, denominador)
        except ValueError as e:
            raise ValueError(f"Entrada inválida para número misto: {e}")

# --- Interface Gráfica com Tkinter ---
class CalculadoraFracao:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Frações - By Mano")
        master.geometry("500x550") # Aumenta um pouco o tamanho da janela
        master.resizable(False, False) # Impede redimensionamento
        master.configure(bg="#F0F0F0") # Cor de fundo padrão da janela

        # Definições de Estilo
        self.FONT_TITLE = ("Helvetica", 16, "bold")
        self.FONT_SUBTITLE = ("Helvetica", 12, "bold")
        self.FONT_TEXT = ("Arial", 10)
        self.FONT_RESULT = ("Consolas", 14, "bold")

        self.COLOR_PRIMARY = "#4CAF50"  # Verde
        self.COLOR_SECONDARY = "#2196F3" # Azul
        self.COLOR_ACCENT = "#FFC107"   # Amarelo
        self.COLOR_BG = "#FFFFFF"       # Branco (para frames internos)
        self.COLOR_LIGHT_GRAY = "#EEEEEE" # Cinza claro
        self.COLOR_DARK_TEXT = "#333333" # Texto escuro

        self.frames = {} 
        self.criar_menu_principal()
        self.criar_frames_operacoes()

        self.mostrar_frame("menu_principal")

    def criar_menu_principal(self):
        menu_frame = tk.Frame(self.master, padx=30, pady=30, bg=self.COLOR_LIGHT_GRAY, relief="raised", borderwidth=3)
        self.frames["menu_principal"] = menu_frame

        tk.Label(menu_frame, text="Calculadora de Frações", font=("Helvetica", 18, "bold"), 
                 bg=self.COLOR_LIGHT_GRAY, fg=self.COLOR_DARK_TEXT).pack(pady=(10, 20))

        tk.Label(menu_frame, text="Escolha uma operação:", font=self.FONT_TITLE, 
                 bg=self.COLOR_LIGHT_GRAY, fg=self.COLOR_PRIMARY).pack(pady=10)

        opcoes = [
            ("Simplificar Fração", "simplificar"),
            ("Operações Aritméticas (+ - * /)", "aritmetica"),
            ("Comparar Frações", "comparacao"),
            ("Conversão Misto ↔ Imprópria", "mistos_improprias")
        ]

        for texto, comando in opcoes:
            tk.Button(menu_frame, text=texto, command=lambda c=comando: self.mostrar_frame(c),
                      font=self.FONT_SUBTITLE, bg=self.COLOR_SECONDARY, fg="white", 
                      width=30, height=2, relief="raised", bd=3,
                      activebackground=self.COLOR_PRIMARY, activeforeground="white").pack(pady=8)
    
    def criar_frames_operacoes(self):
        # --- Frame de Aritmética (Soma, Subtração, Multiplicação, Divisão) ---
        aritmetica_frame = tk.Frame(self.master, padx=20, pady=20, bg=self.COLOR_BG, relief="groove", borderwidth=2)
        self.frames["aritmetica"] = aritmetica_frame

        tk.Label(aritmetica_frame, text="Operações Aritméticas", font=self.FONT_TITLE, 
                 bg=self.COLOR_BG, fg=self.COLOR_PRIMARY).pack(pady=(5, 15))

        # Função auxiliar para criar linhas de entrada de fração
        def criar_entrada_fracao(parent, label_text, num_var, den_var):
            frame = tk.Frame(parent, bg=self.COLOR_BG)
            frame.pack(pady=5)
            tk.Label(frame, text=label_text, font=self.FONT_TEXT, bg=self.COLOR_BG, fg=self.COLOR_DARK_TEXT).pack(side=tk.LEFT)
            tk.Entry(frame, width=7, textvariable=num_var, font=self.FONT_TEXT, justify="center", bd=2, relief="sunken").pack(side=tk.LEFT, padx=2)
            tk.Label(frame, text="/", font=self.FONT_TEXT, bg=self.COLOR_BG, fg=self.COLOR_DARK_TEXT).pack(side=tk.LEFT)
            tk.Entry(frame, width=7, textvariable=den_var, font=self.FONT_TEXT, justify="center", bd=2, relief="sunken").pack(side=tk.LEFT, padx=2)
            return num_var, den_var # Retorna as StringVar para uso posterior

        self.num1_var = tk.StringVar(self.master)
        self.den1_var = tk.StringVar(self.master)
        criar_entrada_fracao(aritmetica_frame, "Fração 1:", self.num1_var, self.den1_var)
        
        # Operação
        frame_op = tk.Frame(aritmetica_frame, bg=self.COLOR_BG)
        frame_op.pack(pady=10)
        tk.Label(frame_op, text="Operação:", font=self.FONT_TEXT, bg=self.COLOR_BG, fg=self.COLOR_DARK_TEXT).pack(side=tk.LEFT)
        self.operacao_var = tk.StringVar(self.master)
        self.operacao_var.set("+") 
        self.operacao_menu = tk.OptionMenu(frame_op, self.operacao_var, "+", "-", "*", "/")
        self.operacao_menu.config(font=self.FONT_TEXT, bg=self.COLOR_ACCENT, fg=self.COLOR_DARK_TEXT, 
                                   activebackground=self.COLOR_PRIMARY, activeforeground="white", relief="raised", bd=2)
        self.operacao_menu.pack(side=tk.LEFT, padx=5)

        self.num2_var = tk.StringVar(self.master)
        self.den2_var = tk.StringVar(self.master)
        criar_entrada_fracao(aritmetica_frame, "Fração 2:", self.num2_var, self.den2_var)

        tk.Button(aritmetica_frame, text="Calcular", command=self.calcular_aritmetica,
                  font=self.FONT_SUBTITLE, bg=self.COLOR_PRIMARY, fg="white", 
                  width=15, height=1, relief="raised", bd=3,
                  activebackground=self.COLOR_ACCENT).pack(pady=15)
        
        tk.Label(aritmetica_frame, text="Resultado:", font=self.FONT_TEXT, 
                 bg=self.COLOR_BG, fg=self.COLOR_DARK_TEXT).pack()
        self.resultado_aritmetica_label = tk.Label(aritmetica_frame, text="Aguardando...", 
                                                    font=self.FONT_RESULT, bg=self.COLOR_BG, fg=self.COLOR_SECONDARY)
        self.resultado_aritmetica_label.pack(pady=5)
        
        tk.Button(aritmetica_frame, text="Voltar ao Menu", command=lambda: self.mostrar_frame("menu_principal"),
                  font=self.FONT_TEXT, bg="#607D8B", fg="white", width=15, relief="flat",
                  activebackground="#455A64").pack(pady=10)

        # --- Frame de Simplificar ---
        simplificar_frame = tk.Frame(self.master, padx=20, pady=20, bg=self.COLOR_BG, relief="groove", borderwidth=2)
        self.frames["simplificar"] = simplificar_frame

        tk.Label(simplificar_frame, text="Simplificar Fração", font=self.FONT_TITLE, 
                 bg=self.COLOR_BG, fg=self.COLOR_PRIMARY).pack(pady=(5, 15))
        
        self.num_simples_var = tk.StringVar(self.master)
        self.den_simples_var = tk.StringVar(self.master)
        criar_entrada_fracao(simplificar_frame, "Fração:", self.num_simples_var, self.den_simples_var)

        tk.Button(simplificar_frame, text="Simplificar", command=self.calcular_simplificar,
                  font=self.FONT_SUBTITLE, bg=self.COLOR_PRIMARY, fg="white", 
                  width=15, height=1, relief="raised", bd=3,
                  activebackground=self.COLOR_ACCENT).pack(pady=15)
        
        tk.Label(simplificar_frame, text="Fração Simplificada:", font=self.FONT_TEXT, 
                 bg=self.COLOR_BG, fg=self.COLOR_DARK_TEXT).pack()
        self.resultado_simplificar_label = tk.Label(simplificar_frame, text="Aguardando...", 
                                                     font=self.FONT_RESULT, bg=self.COLOR_BG, fg=self.COLOR_SECONDARY)
        self.resultado_simplificar_label.pack(pady=5)
        
        tk.Button(simplificar_frame, text="Voltar ao Menu", command=lambda: self.mostrar_frame("menu_principal"),
                  font=self.FONT_TEXT, bg="#607D8B", fg="white", width=15, relief="flat",
                  activebackground="#455A64").pack(pady=10)

        # --- Frame de Comparação ---
        comparacao_frame = tk.Frame(self.master, padx=20, pady=20, bg=self.COLOR_BG, relief="groove", borderwidth=2)
        self.frames["comparacao"] = comparacao_frame

        tk.Label(comparacao_frame, text="Comparar Frações", font=self.FONT_TITLE, 
                 bg=self.COLOR_BG, fg=self.COLOR_PRIMARY).pack(pady=(5, 15))
        
        self.num_comp1_var = tk.StringVar(self.master)
        self.den_comp1_var = tk.StringVar(self.master)
        criar_entrada_fracao(comparacao_frame, "Fração 1:", self.num_comp1_var, self.den_comp1_var)
        
        self.num_comp2_var = tk.StringVar(self.master)
        self.den_comp2_var = tk.StringVar(self.master)
        criar_entrada_fracao(comparacao_frame, "Fração 2:", self.num_comp2_var, self.den_comp2_var)

        tk.Button(comparacao_frame, text="Comparar", command=self.calcular_comparacao,
                  font=self.FONT_SUBTITLE, bg=self.COLOR_PRIMARY, fg="white", 
                  width=15, height=1, relief="raised", bd=3,
                  activebackground=self.COLOR_ACCENT).pack(pady=15)
        
        tk.Label(comparacao_frame, text="Resultado da Comparação:", font=self.FONT_TEXT, 
                 bg=self.COLOR_BG, fg=self.COLOR_DARK_TEXT).pack()
        self.resultado_comparacao_label = tk.Label(comparacao_frame, text="Aguardando...", 
                                                    font=self.FONT_RESULT, bg=self.COLOR_BG, fg=self.COLOR_SECONDARY)
        self.resultado_comparacao_label.pack(pady=5)
        
        tk.Button(comparacao_frame, text="Voltar ao Menu", command=lambda: self.mostrar_frame("menu_principal"),
                  font=self.FONT_TEXT, bg="#607D8B", fg="white", width=15, relief="flat",
                  activebackground="#455A64").pack(pady=10)

        # --- Frame de Números Mistos e Frações Impróprias ---
        mistos_improprias_frame = tk.Frame(self.master, padx=20, pady=20, bg=self.COLOR_BG, relief="groove", borderwidth=2)
        self.frames["mistos_improprias"] = mistos_improprias_frame

        tk.Label(mistos_improprias_frame, text="Números Mistos e Frações Impróprias", font=self.FONT_TITLE, 
                 bg=self.COLOR_BG, fg=self.COLOR_PRIMARY).pack(pady=(5, 15))

        # Conversão de Imprópria para Mista
        tk.Label(mistos_improprias_frame, text="Fração Imprópria para Mista:", font=self.FONT_SUBTITLE, 
                 bg=self.COLOR_BG, fg=self.COLOR_DARK_TEXT).pack(pady=(10, 0))
        
        frame_imp_to_mist = tk.Frame(mistos_improprias_frame, bg=self.COLOR_BG)
        frame_imp_to_mist.pack(pady=5)
        tk.Label(frame_imp_to_mist, text="Numerador:", font=self.FONT_TEXT, bg=self.COLOR_BG, fg=self.COLOR_DARK_TEXT).pack(side=tk.LEFT)
        self.num_imp_var = tk.StringVar(self.master)
        tk.Entry(frame_imp_to_mist, width=7, textvariable=self.num_imp_var, font=self.FONT_TEXT, justify="center", bd=2, relief="sunken").pack(side=tk.LEFT, padx=2)
        tk.Label(frame_imp_to_mist, text="Denominador:", font=self.FONT_TEXT, bg=self.COLOR_BG, fg=self.COLOR_DARK_TEXT).pack(side=tk.LEFT, padx=(10,0))
        self.den_imp_var = tk.StringVar(self.master)
        tk.Entry(frame_imp_to_mist, width=7, textvariable=self.den_imp_var, font=self.FONT_TEXT, justify="center", bd=2, relief="sunken").pack(side=tk.LEFT, padx=2)
        
        tk.Button(mistos_improprias_frame, text="Converter para Misto", command=self.converter_impropria_para_mista,
                  font=self.FONT_TEXT, bg=self.COLOR_ACCENT, fg=self.COLOR_DARK_TEXT, width=20, relief="raised", bd=2,
                  activebackground=self.COLOR_PRIMARY).pack(pady=8)
        self.resultado_imp_to_mist_label = tk.Label(mistos_improprias_frame, text="Aguardando...", 
                                                     font=self.FONT_RESULT, bg=self.COLOR_BG, fg=self.COLOR_SECONDARY)
        self.resultado_imp_to_mist_label.pack(pady=5)

        # Conversão de Mista para Imprópria
        tk.Label(mistos_improprias_frame, text="Número Misto para Fração Imprópria:", font=self.FONT_SUBTITLE, 
                 bg=self.COLOR_BG, fg=self.COLOR_DARK_TEXT).pack(pady=(15, 0))
        
        frame_mist_to_imp = tk.Frame(mistos_improprias_frame, bg=self.COLOR_BG)
        frame_mist_to_imp.pack(pady=5)
        tk.Label(frame_mist_to_imp, text="Inteiro:", font=self.FONT_TEXT, bg=self.COLOR_BG, fg=self.COLOR_DARK_TEXT).pack(side=tk.LEFT)
        self.inteiro_misto_var = tk.StringVar(self.master)
        tk.Entry(frame_mist_to_imp, width=5, textvariable=self.inteiro_misto_var, font=self.FONT_TEXT, justify="center", bd=2, relief="sunken").pack(side=tk.LEFT, padx=2)
        tk.Label(frame_mist_to_imp, text="Numerador:", font=self.FONT_TEXT, bg=self.COLOR_BG, fg=self.COLOR_DARK_TEXT).pack(side=tk.LEFT, padx=(10,0))
        self.num_misto_var = tk.StringVar(self.master)
        tk.Entry(frame_mist_to_imp, width=5, textvariable=self.num_misto_var, font=self.FONT_TEXT, justify="center", bd=2, relief="sunken").pack(side=tk.LEFT, padx=2)
        tk.Label(frame_mist_to_imp, text="/", font=self.FONT_TEXT, bg=self.COLOR_BG, fg=self.COLOR_DARK_TEXT).pack(side=tk.LEFT)
        self.den_misto_var = tk.StringVar(self.master)
        tk.Entry(frame_mist_to_imp, width=5, textvariable=self.den_misto_var, font=self.FONT_TEXT, justify="center", bd=2, relief="sunken").pack(side=tk.LEFT, padx=2)
        
        tk.Button(mistos_improprias_frame, text="Converter para Imprópria", command=self.converter_mista_para_impropria,
                  font=self.FONT_TEXT, bg=self.COLOR_ACCENT, fg=self.COLOR_DARK_TEXT, width=20, relief="raised", bd=2,
                  activebackground=self.COLOR_PRIMARY).pack(pady=8)
        self.resultado_mist_to_imp_label = tk.Label(mistos_improprias_frame, text="Aguardando...", 
                                                     font=self.FONT_RESULT, bg=self.COLOR_BG, fg=self.COLOR_SECONDARY)
        self.resultado_mist_to_imp_label.pack(pady=5)

        tk.Button(mistos_improprias_frame, text="Voltar ao Menu", command=lambda: self.mostrar_frame("menu_principal"),
                  font=self.FONT_TEXT, bg="#607D8B", fg="white", width=15, relief="flat",
                  activebackground="#455A64").pack(pady=10)


    def mostrar_frame(self, nome_frame):
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[nome_frame].pack(fill="both", expand=True)

    # --- Métodos de obtenção de fração com StringVar ---
    def obter_fracao_from_vars(self, num_var, den_var):
        try:
            numerador = int(num_var.get())
            denominador = int(den_var.get())
            return Fracao(numerador, denominador)
        except ValueError as e:
            messagebox.showerror("Erro de Entrada", f"Entrada inválida. Certifique-se de digitar números inteiros. Detalhe: {e}")
            return None

    def calcular_aritmetica(self):
        fracao1 = self.obter_fracao_from_vars(self.num1_var, self.den1_var)
        fracao2 = self.obter_fracao_from_vars(self.num2_var, self.den2_var)

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
            fracao_original = self.obter_fracao_from_vars(self.num_simples_var, self.den_simples_var)
            if fracao_original:
                self.resultado_simplificar_label.config(text=str(fracao_original))
        except Exception as e:
            messagebox.showerror("Erro de Simplificação", str(e))
            self.resultado_simplificar_label.config(text="Erro na simplificação.")

    def calcular_comparacao(self):
        fracao1 = self.obter_fracao_from_vars(self.num_comp1_var, self.den_comp1_var)
        fracao2 = self.obter_fracao_from_vars(self.num_comp2_var, self.den_comp2_var)

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
            fracao_impropria = self.obter_fracao_from_vars(self.num_imp_var, self.den_imp_var)
            if fracao_impropria:
                self.resultado_imp_to_mist_label.config(text=fracao_impropria.para_misto())
        except Exception as e:
            messagebox.showerror("Erro de Conversão", str(e))
            self.resultado_imp_to_mist_label.config(text="Erro na conversão.")

    def converter_mista_para_impropria(self):
        try:
            inteiro_str = self.inteiro_misto_var.get()
            numerador_str = self.num_misto_var.get()
            denominador_str = self.den_misto_var.get()

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