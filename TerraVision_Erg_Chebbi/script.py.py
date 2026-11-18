import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

janela = tk.Tk()
janela.title("TerraVision | Geographic Analysis")
janela.geometry("1200x780")
janela.configure(bg="#171c22")

# Cabeçalho
topo = tk.Frame(janela, bg="#202832", height=75)
topo.pack(fill="x")

tk.Label(
    topo, text="TERRAVISION",
    font=("Arial", 23, "bold"),
    fg="#e6bd80", bg="#202832"
).pack(side="left", padx=25, pady=18)

tk.Label(
    topo, text="GEOGRAPHIC ANALYSIS | ERG CHEBBI",
    font=("Arial", 10),
    fg="white", bg="#202832"
).pack(side="right", padx=25)

# Conteúdo
conteudo = tk.Frame(janela, bg="#171c22")
conteudo.pack(fill="both", expand=True, padx=20, pady=20)

tk.Label(
    conteudo, text="SAHARA DESERT",
    font=("Arial", 24, "bold"),
    fg="#e6bd80", bg="#171c22"
).pack(anchor="w")

tk.Label(
    conteudo, text="Erg Chebbi • Marrocos",
    font=("Arial", 12),
    fg="#c5cbd2", bg="#171c22"
).pack(anchor="w", pady=5)

# Imagem principal
try:
    imagem = Image.open("Erg_Chebbi_Imagem_Satelite.png")
    imagem.thumbnail((1100, 470))
    foto = ImageTk.PhotoImage(imagem)

    painel = tk.Label(conteudo, image=foto, bg="#171c22")
    painel.image = foto
    painel.pack(pady=15)

except Exception as erro:
    tk.Label(
        conteudo,
        text=f"Imagem não encontrada: {erro}",
        fg="red", bg="#171c22"
    ).pack()

# Pesquisa
pesquisa = tk.Entry(conteudo, font=("Arial", 12), width=55)
pesquisa.pack(pady=10)
pesquisa.insert(0, "Pesquisar região geográfica...")

tk.Label(
    conteudo,
    text="ANÁLISE: ZONAS DESÉRTICAS E CAMADAS DE AREIA",
    font=("Arial", 12, "bold"),
    fg="#e6bd80", bg="#171c22"
).pack(pady=10)

janela.mainloop()