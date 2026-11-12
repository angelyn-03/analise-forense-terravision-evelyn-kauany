"""
Projeto TerraVision — Análise Forense e Computação Gráfica
Tema: Zonas Desérticas e Camadas de Areia (Superfícies Uniformes e Dunas)

Função: selecionar o nível de detalhamento (LoD) conforme a altitude
da câmera virtual.
"""

def carregar_camada_satelite(lista_altitudes):
    """
    Recebe uma lista com pelo menos 5 altitudes (em metros), percorre
    os valores e informa qual camada deve ser renderizada.

    Regras:
    - Acima de 10.000 m: baixa resolução.
    - De 1.000 m até 10.000 m: média resolução.
    - Abaixo de 1.000 m: alta resolução.

    Retorna uma lista com os níveis selecionados.
    """
    if not isinstance(lista_altitudes, (list, tuple)):
        raise TypeError("O parâmetro deve ser uma lista ou tupla de altitudes.")

    if len(lista_altitudes) < 5:
        raise ValueError("Informe pelo menos 5 valores de altitude.")

    niveis_renderizacao = []

    for altitude in lista_altitudes:
        if not isinstance(altitude, (int, float)) or isinstance(altitude, bool):
            raise TypeError("Todas as altitudes devem ser números.")

        if altitude < 0:
            raise ValueError("A altitude não pode ser negativa.")

        if altitude > 10000:
            nivel = "Baixa resolução"
            mensagem = (
                f"Altitude: {altitude} m — Baixa resolução: "
                "carregando o mosaico geral da Terra para localizar "
                "as grandes regiões desérticas."
            )
        elif altitude >= 1000:
            nivel = "Média resolução"
            mensagem = (
                f"Altitude: {altitude} m — Média resolução: "
                "carregando o mosaico regional do deserto, com a "
                "distribuição das áreas arenosas e das formações de dunas."
            )
        else:
            nivel = "Alta resolução"
            mensagem = (
                f"Altitude: {altitude} m — Alta resolução: "
                "carregando detalhes das dunas, das camadas de areia, "
                "das ondulações, das texturas e das sombras do terreno."
            )

        print(mensagem)
        niveis_renderizacao.append(nivel)

    return niveis_renderizacao


# Testes com seis altitudes, contemplando os três níveis de renderização.
if __name__ == "__main__":
    altitudes_teste = [15000, 10000, 5000, 1000, 500, 100]

    print("=== TESTE DA FUNÇÃO carregar_camada_satelite ===")
    resultados = carregar_camada_satelite(altitudes_teste)

    print("\n=== RESUMO DOS NÍVEIS SELECIONADOS ===")
    for altitude, nivel in zip(altitudes_teste, resultados):
        print(f"{altitude} m -> {nivel}")
