import tkinter as tk
from interface import InterfaceIMC

if __name__ == "__main__":
    # 1. Cria a janela raiz (root)
    root = tk.Tk()

    # 2. Instancia a nossa classe de Interface, passando a janela raiz
    # Isso inicia o desenho dos botões e a conexão com a lógica
    app = InterfaceIMC(root)

    # 3. Inicia o loop principal (Mantém a janela aberta)
    # O programa só sai daqui quando o usuário fecha a janela
    root.mainloop()