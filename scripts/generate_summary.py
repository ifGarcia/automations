"""
Script auxiliar que invoca o Copilot CLI para analisar o repositório
e gera um arquivo SUMMARY.md com comentários técnicos explicativos.

Uso esperado: executado via GitHub Actions com COPILOT_GITHUB_TOKEN no ambiente.
Risco: depende da disponibilidade do binário `copilot` no PATH e de um token válido.
"""

import os
import subprocess

def main():
    # Prompt enviado ao Copilot CLI — define o escopo da análise.
    # Atenção: erros de digitação no prompt ("comnetrios") não afetam a execução,
    # mas podem degradar a qualidade da resposta do modelo.
    prompt = "Analise este repositório e adicione comnetrios em cada automação. A ideia é ser comentrios tecnicos explicativos."

    # Lê o token de autenticação do ambiente; obrigatório para o Copilot CLI.
    # Nunca exponha este token em logs ou artefatos do workflow.
    token = os.getenv("COPILOT_GITHUB_TOKEN")
    if not token:
        raise RuntimeError("COPILOT_GITHUB_TOKEN não encontrado no ambiente.")

    # Abre o processo do Copilot CLI em modo streaming (Popen).
    # stderr separado permite capturar erros sem misturá-los com a saída útil.
    # A variável COPILOT_GITHUB_TOKEN é injetada explicitamente para garantir
    # que o processo filho a receba, mesmo em ambientes restritivos.
    process = subprocess.Popen(
        ["copilot", "-p", prompt],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env={**os.environ, "COPILOT_GITHUB_TOKEN": token}
    )

    # Lê a saída linha a linha (streaming), evitando carregar tudo na memória.
    # Grava simultaneamente no log da Action e no arquivo SUMMARY.md.
    with open("SUMMARY.md", "w", encoding="utf-8") as f:
        for line in process.stdout:
            print(line, end="")   # mostra no log da Action
            f.write(line)         # grava no arquivo

    # Aguarda o término do processo e verifica o código de saída.
    # Código diferente de 0 indica falha; o stderr é exibido para diagnóstico.
    process.wait()
    if process.returncode != 0:
        print("Erro:", process.stderr.read())

if __name__ == "__main__":
    main()
