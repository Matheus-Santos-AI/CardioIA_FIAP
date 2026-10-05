"""
Sistema simples de apoio ao diagnóstico baseado em um mapa de conhecimento
(ontologia simplificada: sintoma -> doença).

Fluxo:
1. Lê as frases dos pacientes (frases_pacientes.txt)
2. Carrega o mapa de conhecimento (mapa_conhecimento.csv)
3. Identifica, em cada frase, as expressões de sintomas conhecidas
4. Pontua cada doença pelo nº de sintomas distintos encontrados
5. Sugere o(s) diagnóstico(s) mais provável(is)

Uso: python diagnostico_ontologia.py
"""

import csv
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

PASTA = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
ARQ_FRASES = PASTA / "frases_pacientes.txt"
ARQ_MAPA = PASTA / "mapa_conhecimento.csv"
ARQ_SAIDA = PASTA / "resultado_diagnosticos.csv"


def normalizar(texto: str) -> str:
    """Minúsculas, sem acentos e sem pontuação, para facilitar a comparação."""
    texto = unicodedata.normalize("NFD", texto.lower())
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    texto = re.sub(r"[^\w\s]", " ", texto)
    return re.sub(r"\s+", " ", texto).strip()


def carregar_frases(caminho: Path) -> list[str]:
    with open(caminho, encoding="utf-8") as f:
        return [linha.strip() for linha in f if linha.strip()]


def carregar_ontologia(caminho: Path) -> dict[str, set[str]]:
    """
    Retorna {doença: {expressões de sintomas normalizadas}}.
    Cada linha do CSV adiciona Sintoma 1 e Sintoma 2 à doença associada.
    """
    ontologia = defaultdict(set)
    with open(caminho, encoding="utf-8", newline="") as f:
        for linha in csv.DictReader(f):
            doenca = linha["Doença Associada"].strip()
            for coluna in ("Sintoma 1", "Sintoma 2"):
                expressao = normalizar(linha[coluna])
                if expressao:
                    ontologia[doenca].add(expressao)
    return ontologia


def analisar_frase(frase: str, ontologia: dict[str, set[str]]) -> list[tuple[str, list[str]]]:
    """
    Retorna lista de (doença, sintomas_encontrados) ordenada da maior
    para a menor pontuação.
    """
    texto = f" {normalizar(frase)} "  # espaços garantem correspondência de palavra inteira
    resultados = []
    for doenca, expressoes in ontologia.items():
        encontrados = sorted(e for e in expressoes if f" {e} " in texto)
        if encontrados:
            resultados.append((doenca, encontrados))
    resultados.sort(key=lambda r: len(r[1]), reverse=True)
    return resultados


def main():
    frases = carregar_frases(ARQ_FRASES)
    ontologia = carregar_ontologia(ARQ_MAPA)
    saida = []

    for i, frase in enumerate(frases, start=1):
        print(f"\nPaciente {i}: {frase}")
        resultados = analisar_frase(frase, ontologia)

        if not resultados:
            print("  -> Nenhum sintoma reconhecido no mapa de conhecimento.")
            saida.append([i, frase, "", "", "Sem diagnóstico"])
            continue

        melhor_doenca, melhores_sintomas = resultados[0]
        todos_sintomas = sorted({s for _, ss in resultados for s in ss})
        print(f"  Sintomas identificados: {', '.join(todos_sintomas)}")
        print("  Ranking de possíveis diagnósticos:")
        for doenca, sintomas in resultados[:3]:
            print(f"    - {doenca}: {len(sintomas)} sintoma(s) ({', '.join(sintomas)})")
        print(f"  => Diagnóstico sugerido: {melhor_doenca}")

        saida.append([i, frase, "; ".join(todos_sintomas), len(melhores_sintomas), melhor_doenca])

    with open(ARQ_SAIDA, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Paciente", "Frase", "Sintomas identificados", "Pontuação", "Diagnóstico sugerido"])
        w.writerows(saida)

    print(f"\nResultados salvos em: {ARQ_SAIDA.name}")
    print("Aviso: projeto educacional. Não substitui avaliação médica.")


if __name__ == "__main__":
    main()