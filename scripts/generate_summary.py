import os
import subprocess

def main():
    prompt = "Analise este repositório e adicione comnetrios em cada automação. A ideia é ser comentrios tecnicos explicativos."
    output_file = "SUMMARY.md"

    # Recupera o token do ambiente
    token = os.getenv("COPILOT_GITHUB_TOKEN")
    if not token:
        raise RuntimeError("COPILOT_GITHUB_TOKEN não encontrado no ambiente.")

    # Executa o Copilot CLI
    try:
        result = subprocess.run(
            ["copilot", "-p", prompt],
            capture_output=True,
            text=True,
            check=True,
            env={**os.environ, "COPILOT_GITHUB_TOKEN": token}
        )
        # Grava saída no arquivo
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result.stdout)
        print(f"Resumo gerado em {output_file}")
    except subprocess.CalledProcessError as e:
        print("Erro ao executar Copilot CLI:", e.stderr)
        raise

if __name__ == "__main__":
    main()
