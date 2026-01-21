# =========================
# IMPORTAÇÕES
# =========================
import tkinter as tk
from tkinter import filedialog
import os
import random
import base64
from dotenv import load_dotenv

# =========================
# CONFIGURAÇÃO DO .env
# =========================
APPDATA = os.getenv("APPDATA")  # Exemplo: C:\Users\<usuario>\AppData\Roaming
SECRET_DIR = os.path.join(APPDATA, "secret")
ENV_FILE = os.path.join(SECRET_DIR, ".env")

# Garante que a pasta exista
os.makedirs(SECRET_DIR, exist_ok=True)


# =========================
# FUNÇÃO: CRIAR ARQUIVO .env INICIAL
# =========================
def criar_secret_env():
    conteudo = """CHAVE_BASE64=Ty4vw4HDgAokJ3PDh+KAnTjDukTDocOCSCHDg3Usw6DDlUMobkpJw403RmQjJmEpQMOUfTZYXVcwQcOKw6lTaG/DtE5bYkt4w6JneTVfcFAxZTPDs2Y6bCsiakUtWll0a8O1OXE9aVUldj9STUd3UeKAnMOTTDJyVjtte8Onw4ljVHo0QsOaw6Mgw60qCcOq
"""
    with open(ENV_FILE, "w", encoding="utf-8") as f:
        f.write(conteudo)

    print(f"Pasta criada em: {SECRET_DIR}")
    print(f"Arquivo .env criado em: {ENV_FILE}")


# =========================
# LISTA DE CARACTERES PERMITIDOS
# =========================
CARACTERES_BASE = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    " "
    ".,;:!?()[]{}+-*/=_@#$%&"
    "\"'“”"
    "\n\t"
    "áàâãéêíóôõúç"
    "ÁÀÂÃÉÊÍÓÔÕÚÇ"
)


# =========================
# CARREGAR A CHAVE DO .env
# =========================
def carregar_chave():
    load_dotenv(ENV_FILE)  # lê especificamente o arquivo .env nesse diretório

    chave_b64 = os.getenv("CHAVE_BASE64")
    if not chave_b64:
        return None

    try:
        return base64.b64decode(chave_b64).decode("utf-8")
    except Exception:
        return None


# =========================
# SALVAR A CHAVE NO .env
# =========================
def salvar_chave_env(chave):
    if not chave:
        raise ValueError("Chave inválida")

    chave_b64 = base64.b64encode(chave.encode("utf-8")).decode("ascii")

    with open(ENV_FILE, "w", encoding="utf-8") as f:
        f.write(f"CHAVE_BASE64={chave_b64}\n")

    print(f"\n✅ Chave salva com sucesso em: {ENV_FILE}")


# =========================
# GERAR UMA NOVA CHAVE
# =========================
def gerar_chave():
    lista = list(CARACTERES_BASE)
    random.shuffle(lista)

    chave = "".join(lista)

    salvar_chave_env(chave)
    return chave


# =========================
# FUNÇÕES VISUAIS
# =========================
def cabecalho(nome, titulo):
    linha = "=-" * 45
    print(linha)
    print(f"{nome:^{len(linha)}}")
    print(linha)
    print(f"{titulo:^{len(linha)}}")


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


# =========================
# CODIFICAR TEXTO
# =========================
def codificar(texto, chave):
    indices = []
    for char in texto:
        if char not in chave:
            print("⚠️ Não sei codificar:", repr(char))
            continue
        indices.append(str(chave.index(char)))
    return "CODIFY1::" + "|".join(indices)


# =========================
# DECIFRAR TEXTO
# =========================
def decifrar(codigo, chave):
    if not codigo.startswith("CODIFY1::"):
        raise ValueError("Código inválido")

    corpo = codigo.split("::", 1)[1]
    corpo = corpo.replace("\n", "").replace("\r", "")
    numeros = [n for n in corpo.split("|") if n.strip()]

    resultado = []
    for n in numeros:
        resultado.append(chave[int(n)])
    return "".join(resultado)


# =========================
# SALVAR EM ARQUIVO .codify
# =========================
def salvar_em_arquivo(codigo):
    root = tk.Tk()
    root.withdraw()
    caminho = filedialog.asksaveasfilename(
        title="Salvar arquivo Codify",
        defaultextension=".codify",
        filetypes=[
            ("Arquivo Codify", "*.codify"),
            ("Arquivo Texto", "*.txt"),
            ],
    )
    if not caminho:
        print("Salvamento cancelado.")
        return
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(codigo)
    print(f"Arquivo salvo com sucesso em:\n{caminho}")


# =========================
# CARREGAR ARQUIVO .codify
# =========================
def carregar_arquivo():
    root = tk.Tk()
    root.withdraw()
    caminho = filedialog.askopenfilename(
        title="Abrir arquivo",
        filetypes=[
            ("Arquivo Codify", "*.codify"),
            ("Arquivo Texto", "*.txt"),
            ("Todos os arquivos", "*.*"),
        ],
    )
    if not caminho:
        print("Abertura cancelada.")
        return None
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")
        return None


# =========================
# MENU PRINCIPAL
# =========================
def menu():
    chave = carregar_chave()
    if chave is None:
        print("🔑 Criando chave secreta...\n")
        chave = gerar_chave()
        limpar_tela()

    while True:
        cabecalho("Codify - Codificador de Texto", "-=<   Menu   >=-")
        opcao = input(
            "1 - Codificar\n"
            "2 - Decifrar\n"
            "3 - Codificar Arquivo\n"
            "4 - Decifrar Arquivo\n"
            "5 - Criar nova chave\n"
            "0 - Sair\n"
            "Opção: "
        )

        if opcao == "1":
            limpar_tela()
            cabecalho("Codify - Codificador de Texto", "-=<   Codificar   >=-")
            print("Digite seu texto:")
            linhas = []
            while True:
                linha = input()
                if linha.strip().upper() == "FIM":
                    break
                linhas.append(linha)
            texto = "\n".join(linhas)
            print("\n🔐 Resultado:\n")
            texto_codificado = codificar(texto, chave)
            print(texto_codificado)
            print(
                "\nPressione Enter para salvar o texto Codificado em um arquivo .codify"
            )
            salvar_em_arquivo(texto_codificado)
            input("\nPressione Enter...")

        elif opcao == "2":
            limpar_tela()
            cabecalho("Codify - Codificador de Texto", "-=<   Decifrar   >=-")
            codigo = input("Cole o código:\n")
            try:
                print("\n🔓 Texto original:\n")
                print(decifrar(codigo, chave))
            except Exception as e:
                print("\n❌ Erro:", e)
            input("\nEnter para voltar...")
            limpar_tela()

        elif opcao == "3":
            cabecalho("Codify - Codificador de Texto", "-=<   Codificar Arquivo   >=-")
            print("Pressione Enter para abrir o arquivo")
            texto = carregar_arquivo()
            if texto:
                print("\n🔓 Texto original:\n")
                print(texto)
                texto_codificado = codificar(texto, chave)
                print("\n🔐 Texto Codificado:\n")
                print(texto_codificado)
                salvar_em_arquivo(texto_codificado)
                input("\nPressione Enter...")
            else:
                input("\nPressione Enter para voltar ao menu...")
                limpar_tela()

        elif opcao == "4":
            limpar_tela()
            cabecalho("Codify - Codificador de Texto", "-=<   Decifrar Arquivo   >=-")
            input("Pressione Enter para carregar o arquivo")
            codigo = carregar_arquivo()
            if codigo:
                texto = decifrar(codigo, chave)
                print("\n🔓 Texto original:\n")
                print(texto)
                salvar_em_arquivo(texto)
                input("\nPressione Enter...")
            else:
                input("\nPressione Enter para voltar ao menu...")
                limpar_tela()

        elif opcao == "5":
            limpar_tela()
            cabecalho("Codify - Codificador de Texto", "-=<   Nova Chave   >=-")
            chave = gerar_chave()
            input("\nEnter para voltar...")
            limpar_tela()

        elif opcao == "0":
            print("\n👋 Até mais!")
            break

        else:
            limpar_tela()


# =========================
# INÍCIO DO PROGRAMA
# =========================

if __name__ == "__main__":
    limpar_tela()
    menu()
