import tkinter as tk
import subprocess

def abrir_instapicker_japones():
    subprocess.Popen(["python", "instapickerjapones1280.py"])

def abrir_instapicker_portugues():
    subprocess.Popen(["python", "instapickerportugues1920.py"])

# Crie a janela da interface gráfica
janela = tk.Tk()
janela.title("Selecionar Versão do Instapicker")

# Botão para abrir o instapicker japonês
botao_japones = tk.Button(janela, text="Abrir Instapicker Japonês", command=abrir_instapicker_japones)
botao_japones.pack(pady=10)

# Botão para abrir o instapicker português
botao_portugues = tk.Button(janela, text="Abrir Instapicker Português", command=abrir_instapicker_portugues)
botao_portugues.pack(pady=10)

# Inicie a janela
janela.mainloop()
