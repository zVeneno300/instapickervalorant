import tkinter as tk
import pyautogui
import time


coordenadas = {
"kayo": (1380, 930), 
"astra": (544, 930), 
"viper": (1300, 1008),
"omen": (714, 1008), 
"kj": (544, 1008), 
"gekko": (1131, 930),
"cypher": (875, 930), 
"jett": (1300, 930), 
"skye": (1131, 1008),
"sage": (1046, 1008), 
"sova": (1216, 1008), 
"chamber": (788, 930),
"dead": (963, 930), 
"neon": (629, 1008), 
"harbor": (1216, 930),
"fade": (1046, 930), 
"phoenix": (788, 1008), 
"breach": (629, 930),
"brimstone": (714, 930), 
"yoru": (1380, 1008), 
"raze": (875, 1008),
"reyna": (963, 1008), 
"fixas": (966, 814)

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


cores_linhas = [ "#00C4A6", "#721CFF", "#BB6EFF", "#005084", "#E1604B"]


janela = tk.Tk()
janela.title("portugues1920x1080")


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


def selecionar_opcao(nome):
    global opcao_selecionada
    opcao_selecionada = nome


def iniciar_com_tecla(event):
    if event.char.lower() == "p":
        iniciar_programa()


janela.bind("<Key>", iniciar_com_tecla)


janela.mainloop()
