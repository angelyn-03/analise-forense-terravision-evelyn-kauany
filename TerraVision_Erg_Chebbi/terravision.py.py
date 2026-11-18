
import tkinter as tk
from tkinter import ttk

# TERRAVISION 2.0 - ERG CHEBBI

janela = tk.Tk()
janela.title("TerraVision | Geographic Analysis")
janela.geometry("1200x780")
janela.configure(bg="#171c22")
janela.minsize(950, 650)

zoom = 1.0

# CORES
FUNDO = "#171c22"
PAINEL = "#222b33"
DOURADO = "#d9ad70"
TEXTO = "#f4eee5"
AREIA = "#d5a15e"

# CABECALHO
topo = tk.Frame(janela, bg=PAINEL, height=85)
topo.pack(fill="x")
topo.pack_propagate(False)

tk.Label(
    topo, text="TERRAVISION",
    font=("Arial", 25, "bold"),
    fg=DOURADO, bg=PAINEL
).pack(side="left", padx=30, pady=20)

tk.Label(
    topo, text="GEOGRAPHIC INTELLIGENCE  /  MOROCCO",
    font=("Arial", 10),
    fg=TEXTO, bg=PAINEL
).pack(side="right", padx=30)

# CONTEUDO
principal = tk.Frame(janela, bg=FUNDO)
principal.pack(fill="both", expand=True, padx=25, pady=20)

tk.Label(
    principal,
    text="ERG CHEBBI",
    font=("Arial", 23, "bold"),
    fg=TEXTO, bg=FUNDO
).pack(anchor="w")

tk.Label(
    principal,
    text="SAHARA DESERT  |  MOROCCO",
    font=("Arial", 10),
    fg=DOURADO, bg=FUNDO
).pack(anchor="w", pady=(3, 15))

# VISUALIZACAO
visual = tk.Frame(principal, bg=PAINEL)
visual.pack(fill="both", expand=True)

canvas = tk.Canvas(
    visual, bg="#d8a568",
    highlightthickness=0
)
canvas.pack(fill="both", expand=True, padx=8, pady=8)

def desenhar_dunas():
    canvas.delete("all")

    w = max(canvas.winfo_width(), 800)
    h = max(canvas.winfo_height(), 400)

    canvas.create_rectangle(0, 0, w, h, fill="#e7bd83", outline="")

    # Horizonte
    canvas.create_rectangle(
        0, 0, w, h * 0.32,
        fill="#d9b88d", outline=""
    )

    # Dunas
    cores = ["#bd793e", "#d4944e", "#e3ad66", "#c98745", "#e8b978"]

    for i, cor in enumerate(cores):
        base = h * (0.45 + i * 0.12)
        pontos = [
            0, base,
            w * 0.20, base - 100 * zoom,
            w * 0.48, base - 20 * zoom,
            w * 0.72, base - 115 * zoom,
            w, base - 35 * zoom,
            w, h, 0, h
        ]

        canvas.create_polygon(
            pontos, fill=cor, outline=""
        )

    canvas.create_text(
        25, 25, anchor="nw",
        text=f"ERG CHEBBI  |  ZOOM {zoom:.1f}x",
        font=("Arial", 15, "bold"),
        fill="#49301e"
    )

    canvas.create_text(
        25, h - 25, anchor="sw",
        text="SATELLITE TERRAIN SIMULATION",
        font=("Arial", 9, "bold"),
        fill="#49301e"
    )

def aumentar():
    global zoom
    zoom = min(zoom + 0.2, 3.0)
    desenhar_dunas()

def diminuir():
    global zoom
    zoom = max(zoom - 0.2, 0.6)
    desenhar_dunas()

# CONTROLES
controles = tk.Frame(principal, bg=FUNDO)
controles.pack(fill="x", pady=15)

def botao(texto, comando):
    return tk.Button(
        controles, text=texto,
        command=comando,
        bg="#9c693b", fg="white",
        activebackground=DOURADO,
        font=("Arial", 10, "bold"),
        relief="flat", padx=18, pady=9,
        cursor="hand2"
    )

botao("ZOOM +", aumentar).pack(side="left", padx=(0, 8))
botao("ZOOM -", diminuir).pack(side="left")

# INFORMACOES
dados = tk.Frame(principal, bg=PAINEL)
dados.pack(fill="x", pady=5)

informacoes = [
    ("LOCALIZACAO", "Erg Chebbi"),
    ("REGIAO", "Saara"),
    ("PAIS", "Marrocos"),
    ("ALTITUDE", "Aprox. 350 m"),
    ("TERRENO", "Dunas de areia")
]

for titulo, valor in informacoes:
    bloco = tk.Frame(dados, bg=PAINEL)
    bloco.pack(side="left", expand=True, pady=18)

    tk.Label(
        bloco, text=titulo,
        font=("Arial", 8, "bold"),
        fg=DOURADO, bg=PAINEL
    ).pack()

    tk.Label(
        bloco, text=valor,
        font=("Arial", 11, "bold"),
        fg=TEXTO, bg=PAINEL
    ).pack(pady=5)

# RODAPE
tk.Label(
    janela,
    text="TERRAVISION © 2026  |  COMPUTACAO GRAFICA E CIENCIA DE DADOS",
    font=("Arial", 9),
    fg="#9ba5ae", bg=FUNDO
).pack(pady=12)

janela.after(300, desenhar_dunas)
janela.mainloop()
