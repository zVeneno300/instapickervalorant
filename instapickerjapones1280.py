import tkinter as tk
import pyautogui
import time
import threading
import keyboard  

coordenadas = {
    "kayo": (220, 930), "astra": (300, 930), "viper": (380, 930),
    "omen": (472, 930), "kj": (561, 930), "gekko": (645, 930),
    "cypher": (730, 930), "jett": (810, 930), "skye": (894, 930),
    "sage": (982, 930), "sova": (1060, 930), "chamber": (220, 1006),
    "dead": (300, 1006), "neon": (380, 1006), "harbor": (472, 1006),
    "fade": (561, 1006), "phoenix": (645, 1006), "breach": (730, 1006),
    "brimstone": (810, 1006), "yoru": (894, 1006), "raze": (982, 1006),
    "reyna": (1060, 1006), "fixas": (647, 810)
}

opcao_selecionada = None
executando = False

def iniciar_programa():
    global executando
    executando = True
    inicio = time.time()

    time.sleep(3)
    
    while executando:
        if time.time() - inicio > 15:
            executando = False
            break
        
        if opcao_selecionada in coordenadas:
            x, y = coordenadas[opcao_selecionada]
            pyautogui.click(x=x, y=y)
            time.sleep(0.005)
            pyautogui.click(x=coordenadas["fixas"][0], y=coordenadas["fixas"][1])
            time.sleep(0.005)

nomes_opcoes = [
    "kayo", "astra", "viper", "omen", "kj", "gekko", "cypher", "jett", "skye",
    "sage", "sova", "chamber", "dead", "neon", "harbor", "fade", "phoenix",
    "breach", "brimstone", "yoru", "raze", "reyna"
]

cores_fixas = [
    "blue", "green", "skyblue", "red", "yellow", "pink", "purple", "orange", "brown",
    "violet", "cyan", "magenta", "lime", "turquoise", "indigo", "olive", "gold",
    "teal", "maroon", "coral", "slategray", "darkorchid"
]

cores_linhas = ["#00C4A6", "#721CFF", "#BB6EFF", "#005084", "#E1604B"]

janela = tk.Tk()
janela.title("japones1280x1080")

for i in range(5):
    janela.grid_columnconfigure(i, weight=1)

botoes_opcao = []
for nome_opcao, cor in zip(nomes_opcoes, cores_fixas):
    botao = tk.Button(janela, text=nome_opcao, command=lambda nome=nome_opcao: selecionar_opcao(nome), bg=cor, width=15, height=3)
    linha = nomes_opcoes.index(nome_opcao)//5
    coluna = nomes_opcoes.index(nome_opcao)%5
    botao.grid(row=linha, column=coluna, padx=5, pady=5)
    botoes_opcao.append(botao)

    if linha < len(cores_linhas):
        botao.configure(bg=cores_linhas[linha])

botao_iniciar = tk.Button(janela, text="Iniciar", command=iniciar_programa)
botao_iniciar.grid(row=6, column=0, columnspan=5, pady=10)

label_tecla_iniciar = tk.Label(janela, text="Atalho Iniciar: 9")
label_tecla_iniciar.grid(row=7, column=0, padx=5, pady=5)

label_tecla_parar = tk.Label(janela, text="Atalho Parar: 0")
label_tecla_parar.grid(row=7, column=3, padx=5, pady=5)

def selecionar_opcao(nome):
    global opcao_selecionada
    opcao_selecionada = nome

def parar_loop():
    global executando
    executando = False

def iniciar_loop():
    global thread_loop
    thread_loop = threading.Thread(target=iniciar_programa)
    thread_loop.start()

keyboard.add_hotkey('9', iniciar_loop)
keyboard.add_hotkey('0', parar_loop)

janela.mainloop()
