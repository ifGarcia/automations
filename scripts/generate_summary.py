"""
Script de geração de resumo via Copilot CLI.
Invoca o agente Copilot com um prompt fixo e salva a resposta em SUMMARY.md.
Executado como step de um workflow GitHub Actions.
"""

import os
import subprocess

def main():
    # Prompt enviado ao Copilot CLI para análise e comentários no repositório
    prompt = "Analise este repositório e adicione comnetrios em cada automação. A ideia é ser comentrios tecnicos explicativos."

    # O token é injetado pelo runner via secret; nunca hardcode credenciais aqui
    token = os.getenv("COPILOT_GITHUB_TOKEN")
    if not token:
        raise RuntimeError("COPILOT_GITHUB_TOKEN não encontrado no ambiente.")

    # Inicia o processo do Copilot CLI em modo não-interativo com streaming de saída
    # stdout=PIPE permite leitura linha a linha sem bloquear o processo principal
    process = subprocess.Popen(
        ["copilot", "-p", prompt],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env={**os.environ, "COPILOT_GITHUB_TOKEN": token}
    )

    # Lê a saída em streaming: exibe no log da Action e grava no arquivo simultaneamente
    # Evita carregar toda a resposta na memória de uma vez (útil para respostas longas)
    with open("SUMMARY.md", "w", encoding="utf-8") as f:
        for line in process.stdout:
            print(line, end="")   # mostra no log da Action
            f.write(line)         # grava no arquivo

    # Aguarda o processo encerrar e verifica o código de retorno
    process.wait()
    if process.returncode != 0:
        # Lê stderr apenas em caso de falha para não misturar com a saída normal
        print("Erro:", process.stderr.read())

if __name__ == "__main__":
    main()
