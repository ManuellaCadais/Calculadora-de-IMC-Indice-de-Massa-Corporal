import tkinter as tk
from tkinter import messagebox  # Para janelas de erro pop-up
from imc_core import CalculadoraIMC  # Importação da nossa lógica

class InterfaceIMC:
    def __init__(self, master):
        """
        Construtor da Interface.
        :param master: A janela principal (root) do Tkinter.
        """
        self.master = master
        self.master.title("Calculadora de IMC")
        self.master.geometry("350x400")
        self.master.resizable(False, False)

        # 1. Instanciar a Lógica (Conexão Backend-Frontend)
        self.logica = CalculadoraIMC()

        # 2. Construção dos Widgets (Componentes Visuais)
        self._criar_componentes()

    def _criar_componentes(self):
        """Método auxiliar para organizar o layout."""
        
        # Título / Cabeçalho
        titulo = tk.Label(
            self.master, 
            text="Cálculo de IMC", 
            font=("Helvetica", 16, "bold"),
            pady=20
        )
        titulo.pack()

        # Input: Peso
        lbl_peso = tk.Label(self.master, text="O seu Peso (kg):", font=("Arial", 11))
        lbl_peso.pack(pady=(10, 0))

        self.entry_peso = tk.Entry(self.master, font=("Arial", 12), justify="center")
        self.entry_peso.pack(pady=5)

        # Input: Altura
        lbl_altura = tk.Label(self.master, text="A sua Altura (m):", font=("Arial", 11))
        lbl_altura.pack(pady=(10, 0))

        self.entry_altura = tk.Entry(self.master, font=("Arial", 12), justify="center")
        self.entry_altura.pack(pady=5)
        # Dica visual para o utilizador
        lbl_dica = tk.Label(self.master, text="(Ex: 1.75 ou 1,75)", font=("Arial", 8), fg="gray")
        lbl_dica.pack()

        # Botão de Ação
        btn_calcular = tk.Button(
            self.master, 
            text="CALCULAR IMC", 
            command=self.realizar_calculo,  # Vínculo com o evento
            font=("Arial", 10, "bold"),
            bg="#4CAF50", 
            fg="white",
            padx=10, 
            pady=5,
            cursor="hand2"  # Muda o cursor para mãozinha
        )
        btn_calcular.pack(pady=20)

        # Output: Área de Resultado
        self.lbl_resultado_valor = tk.Label(
            self.master, 
            text="---", 
            font=("Helvetica", 20, "bold"), 
            fg="#333"
        )
        self.lbl_resultado_valor.pack()

        self.lbl_resultado_texto = tk.Label(
            self.master, 
            text="A aguardar dados...", 
            font=("Arial", 12, "italic"),
            fg="#666"
        )
        self.lbl_resultado_texto.pack(pady=5)

    def realizar_calculo(self):
        """
        Método acionado pelo clique do botão.
        Recolhe dados -> Chama a Lógica -> Atualiza a Tela.
        """
        # 1. INPUT (Recolha)
        peso = self.entry_peso.get()
        altura = self.entry_altura.get()

        # 2. PROCESSAMENTO (Chama o imc_core.py)
        # O método processar_dados devolve um dicionário pronto
        resultado = self.logica.processar_dados(peso, altura)

        # 3. OUTPUT (Atualização da Interface)
        if resultado["sucesso"]:
            # Se correu tudo bem
            valor_imc = resultado["imc"]
            texto_classificacao = resultado["texto"]

            self.lbl_resultado_valor.config(text=f"{valor_imc:.2f}", fg="#000")
            self.lbl_resultado_texto.config(text=texto_classificacao, fg="blue")
            
            # Muda a cor conforme a gravidade (Opcional, mas fica bonito)
            if "Obesidade" in texto_classificacao:
                self.lbl_resultado_texto.config(fg="red")
            elif "Normal" in texto_classificacao:
                self.lbl_resultado_texto.config(fg="green")
                
        else:
            # Se houve erro (ex: letras no lugar de números)
            erro_msg = resultado["erro"]
            messagebox.showerror("Erro de Entrada", erro_msg)
            
            # Limpa o resultado anterior visualmente
            self.lbl_resultado_valor.config(text="Erro")
            self.lbl_resultado_texto.config(text="Verifique os dados", fg="red")