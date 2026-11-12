
"""
Projeto TerraVision — Análise Forense e Computação Gráfica

Tema: Zonas Desérticas e Camadas de Areia
Local: Erg Chebbi, Merzouga, Marrocos.

Simulação dos níveis de detalhamento (LoD)
conforme a altitude da câmera virtual.
"""

from pathlib import Path
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


# Localização dos arquivos na mesma pasta do script
PASTA_PROJETO = Path(__file__).resolve().parent

IMAGEM_SATELITE = PASTA_PROJETO / "Erg_Chebbi_Imagem_Satelite.png"
IMAGEM_ILUSTRATIVA = PASTA_PROJETO / "Erg_Chebbi_Por_do_Sol.png"


def carregar_camada_satelite(lista_altitudes):
    """
    Recebe pelo menos cinco altitudes e seleciona
    o nível de detalhamento correspondente.
    """

    if not isinstance(lista_altitudes, (list, tuple)):
        raise TypeError("Informe uma lista ou tupla de altitudes.")

    if len(lista_altitudes) < 5:
        raise ValueError("Informe pelo menos 5 altitudes.")

    niveis_renderizacao = []

    for altitude in lista_altitudes:

        if not isinstance(altitude, (int, float)) or isinstance(altitude, bool):
            raise TypeError("As altitudes devem ser números.")

        if altitude < 0:
            raise ValueError("A altitude não pode ser negativa.")

        if altitude > 10000:
            nivel = "Baixa resolução"

        elif altitude >= 1000:
            nivel = "Média resolução"

        else:
            nivel = "Alta resolução"

        print(f"Altitude: {altitude} m -> {nivel}")
        niveis_renderizacao.append(nivel)

    return niveis_renderizacao


def preparar_imagem(imagem, nivel):
    """
    Simula diferentes níveis de detalhamento
    por meio da redução e ampliação da resolução.
    """

    largura, altura = imagem.size

    escalas = {
        "Baixa resolução": 0.12,
        "Média resolução": 0.40,
        "Alta resolução": 1.0
    }

    escala = escalas[nivel]

    if escala == 1.0:
        resultado = imagem.copy()

    else:
        nova_largura = max(1, int(largura * escala))
        nova_altura = max(1, int(altura * escala))

        reduzida = imagem.resize(
            (nova_largura, nova_altura),
            Image.Resampling.BILINEAR
        )

        resultado = reduzida.resize(
            (largura, altura),
            Image.Resampling.NEAREST
        )

    resultado.thumbnail((680, 450))

    return resultado


def abrir_visualizador():
    """
    Abre uma janela para visualizar a imagem
    de satélite em diferentes níveis de detalhamento.
    """

    if not IMAGEM_SATELITE.exists():
        messagebox.showerror(
            "Imagem não encontrada",
            f"Não foi possível encontrar:\n{IMAGEM_SATELITE.name}"
        )
        return

    if not IMAGEM_ILUSTRATIVA.exists():
        messagebox.showerror(
            "Imagem não encontrada",
            f"Não foi possível encontrar:\n{IMAGEM_ILUSTRATIVA.name}"
        )
        return

    satelite = Image.open(IMAGEM_SATELITE).convert("RGB")
    ilustrativa = Image.open(IMAGEM_ILUSTRATIVA).convert("RGB")

    janela = tk.Tk()
    janela.title("TerraVision - Erg Chebbi, Marrocos")
    janela.geometry("1100x750")

    titulo = tk.Label(
        janela,
        text="TERRAVISION - ANÁLISE DE NÍVEIS DE DETALHAMENTO",
        font=("Arial", 15, "bold")
    )
    titulo.pack(pady=12)

    subtitulo = tk.Label(
        janela,
        text="Região analisada: Erg Chebbi, Deserto do Saara, Marrocos",
        font=("Arial", 11)
    )
    subtitulo.pack(pady=5)

    area = tk.Frame(janela)
    area.pack(pady=10)

    quadro_satelite = tk.Frame(area)
    quadro_satelite.grid(row=0, column=0, padx=15)

    quadro_referencia = tk.Frame(area)
    quadro_referencia.grid(row=0, column=1, padx=15)

    tk.Label(
        quadro_satelite,
        text="Imagem de satélite - Google Earth",
        font=("Arial", 11, "bold")
    ).pack(pady=5)

    tk.Label(
        quadro_referencia,
        text="Imagem ilustrativa - Erg Chebbi",
        font=("Arial", 11, "bold")
    ).pack(pady=5)

    painel_satelite = tk.Label(quadro_satelite)
    painel_satelite.pack()

    painel_ilustrativo = tk.Label(quadro_referencia)
    painel_ilustrativo.pack()

    imagem_ref = ilustrativa.copy()
    imagem_ref.thumbnail((350, 350))

    foto_referencia = ImageTk.PhotoImage(imagem_ref)
    painel_ilustrativo.configure(image=foto_referencia)
    painel_ilustrativo.image = foto_referencia

    informacao = tk.Label(
        janela,
        text="Selecione uma altitude para visualizar o nível de detalhamento.",
        font=("Arial", 11)
    )
    informacao.pack(pady=15)

    def selecionar_nivel(altitude, nivel):

        imagem_processada = preparar_imagem(satelite, nivel)

        foto = ImageTk.PhotoImage(imagem_processada)

        painel_satelite.configure(image=foto)
        painel_satelite.image = foto

        informacao.configure(
            text=f"Altitude: {altitude} m | Nível selecionado: {nivel}"
        )

        print(f"Visualização: {altitude} m - {nivel}")

    botoes = tk.Frame(janela)
    botoes.pack(pady=15)

    tk.Button(
        botoes,
        text="Baixa resolução\nAcima de 10.000 m",
        command=lambda: selecionar_nivel(15000, "Baixa resolução"),
        width=22,
        height=3
    ).grid(row=0, column=0, padx=8)

    tk.Button(
        botoes,
        text="Média resolução\nDe 1.000 a 10.000 m",
        command=lambda: selecionar_nivel(5000, "Média resolução"),
        width=22,
        height=3
    ).grid(row=0, column=1, padx=8)

    tk.Button(
        botoes,
        text="Alta resolução\nAbaixo de 1.000 m",
        command=lambda: selecionar_nivel(500, "Alta resolução"),
        width=22,
        height=3
    ).grid(row=0, column=2, padx=8)

    selecionar_nivel(5000, "Média resolução")

    janela.mainloop()


# Execução e testes
if __name__ == "__main__":

    altitudes_teste = [15000, 10000, 5000, 1000, 500, 100]

    print("=== TESTE DA FUNÇÃO TERRAVISION ===")

    resultados = carregar_camada_satelite(altitudes_teste)

    print("\n=== RESUMO DOS NÍVEIS SELECIONADOS ===")

    for altitude, nivel in zip(altitudes_teste, resultados):
        print(f"{altitude} m -> {nivel}")

    abrir_visualizador()
