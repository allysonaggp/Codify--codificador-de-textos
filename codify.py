import os
import random
from dotenv import load_dotenv

load_dotenv()
chave = os.getenv("CHAVE")


# Função para exibir o cabeçalho
def cabecalho(nome):
    linha = "=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
    print(linha)
    print(f"{nome:^{len(linha)}}")
    print(linha)
# Função para gerar uma chave embaralhada
def gerar_chave():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 áéíóúÁÉÍÓÚâêôÂÊÔãõÃÕçÇ,.!?;:@-_()\n'"
    lista_caracteres = list(caracteres)
    random.shuffle(lista_caracteres)
    chave_embaralhada = "".join(lista_caracteres)
    print(chave_embaralhada)


# Função do menu
def menu():
    while True:
        cabecalho("Codificador de Texto")
        menu = input(
            "Escolha uma opção:\n1 - Codificar\n2 - Decifrar\n3 - Gerar Chave \n0 - Sair \nOpção: "
        )
        if menu == "1":

            limpar_tela()
            cabecalho("Codificador de Texto")
            print("Digite seu texto (pressione Enter para nova linha, digite FIM para terminar):")

            linhas = []
            while True:
                linha = input()
                if linha.strip().upper() == "FIM":
                    break
                linhas.append(linha)

            texto = "\n".join(linhas)

            texto_encriptado = codificar(texto)
            print(f"\nTexto encriptado\n{texto_encriptado}")
            input("\nPressione Enter para voltar ao menu...")
            limpar_tela()

        elif menu == "2":

            limpar_tela()
            cabecalho("Codificador de Texto")
            entrada = input("Digite o texto para Decifrar:\n")
            lista = [int(x.strip()) for x in entrada.strip("[]").split(",")]
            texto_decifrado = decifrar(lista)
            limpar_tela()
            cabecalho("Codificador de Texto")
            print("Texto Decifrado")
            print(texto_decifrado)
            input("\nPressione Enter para voltar ao menu...")
            limpar_tela()

        elif menu == "3":

            limpar_tela()
            cabecalho("Codificador de Texto")
            print("Gerando nova chave...")
            gerar_chave()
            input("\nPressione Enter para voltar ao menu...")
            limpar_tela()

        elif menu == "0":

            limpar_tela()
            cabecalho("Codificador de Texto")
            print("Saindo...")
            exit()

        else:
            limpar_tela()
              


# Função para sair do programa
def sair():
    input("\nPressione Enter para sair...")
    exit()


# Função para limpar a tela
def limpar_tela():

    os.system("cls" if os.name == "nt" else "clear")


# Função para encriptar
def codificar(texto):
    resultado = []
    for char in texto:
        resultado.append(chave.index(char))

    return resultado


# Função para decifrar
def decifrar(lista):
    resultado = []
    for valor in lista:
        resultado.append(chave[valor])
    texto = "".join(resultado)

    return texto


# Execução

limpar_tela()
menu()
open
