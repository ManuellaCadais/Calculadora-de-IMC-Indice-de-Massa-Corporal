# Calculadora de IMC - Desktop

## 📋 Sobre o Projeto
Este sistema é uma aplicação desktop desenvolvida em Python para o cálculo do Índice de Massa Corporal (IMC). O objetivo do projeto foi aplicar conceitos de Programação Orientada a Objetos (POO), garantindo uma separação estrita entre a lógica de cálculo (Backend) e a apresentação visual (Frontend).

O programa permite que o usuário insira seu peso e altura, processa os dados e retorna não apenas o valor numérico do IMC, mas também a classificação oficial (ex: Peso Normal, Sobrepeso, Obesidade).

## 👥 Integrantes
* **Manuella Cadais**
* **Leticia**

## ⚙️ Funcionalidades
O sistema obedece ao fluxo de processamento exigido:

1.  **Input:** O usuário insere o Peso (kg) e a Altura (m) na interface.
2.  **Processamento:** O sistema valida se os inputs são números e aplica a fórmula (Peso / Altura²).
3.  **Output:** O sistema exibe o resultado formatado e a categoria de saúde correspondente na tela.

## 🏗️ Arquitetura e POO
O código está dividido em três partes para atender aos critérios de avaliação:

1.  **Lógica (`imc_core.py`):** Contém a classe `CalculadoraIMC`. Ela recebe os valores, faz a conta matemática e decide a classificação. Ela não sabe que existe uma interface gráfica.
2.  **Interface (`interface.py`):** Contém a classe `JanelaPrincipal` usando **Tkinter**. Ela desenha os botões e campos, captura o clique do usuário e "chama" a classe de lógica.
3.  **Execução (`main.py`):** Arquivo simples que apenas instancia a interface e inicia o programa.

## 🚀 Como Executar
1.  Certifique-se de ter o Python 3 instalado.
2.  Baixe os arquivos do projeto.
3.  Abra o terminal na pasta do projeto.
4.  Execute o comando:
    ```bash
    python main.py
    ```

## 🛠️ Tecnologias
* **Linguagem:** Python 3.13.7+
* **Interface Gráfica:** Tkinter (Biblioteca padrão do Python)
* **Paradigma:** Orientação a Objetos

---
*Projeto Final - 3 de Dezembro de 2025*
