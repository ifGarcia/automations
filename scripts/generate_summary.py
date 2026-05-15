import os
import subprocess

def main():
    prompt = "Analise este repositório e adicione comnetrios em cada automação. A ideia é ser comentrios tecnicos explicativos."
    token = os.getenv("COPILOT_GITHUB_TOKEN")
    if not token:
        raise RuntimeError("COPILOT_GITHUB_TOKEN não encontrado no ambiente.")

    process = subprocess.Popen(
        ["copilot", "-p", prompt],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env={**os.environ, "COPILOT_GITHUB_TOKEN": token}
    )

    with open("SUMMARY.md", "w", encoding="utf-8") as f:
        for line in process.stdout:
            print(line, end="")   # mostra no log da Action
            f.write(line)         # grava no arquivo

    process.wait()
    if process.returncode != 0:
        print("Erro:", process.stderr.read())

if __name__ == "__main__":
    main()
