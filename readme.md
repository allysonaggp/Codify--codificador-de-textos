# 🔐Codify-Codificador de Texto

Um eficiente **codificador e decodificador de texto em Python**, feito para transformar mensagens em listas de números e depois decifrá-las novamente usando uma Chave de codificação.  
Ideal para estudos de criptografia básica, lógica de programação e manipulação de strings em Python.

---

## 📖 Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Como Funciona](#como-funciona)
- [Como Executar](#como-executar)
- [Opções do Menu](#opções-do-menu)
- [Exemplo de Uso](#exemplo-de-uso)
- [Detalhes Técnicos](#detalhes-técnicos)
- [Possíveis Erros e Soluções](#possíveis-erros-e-soluções)
- [Melhorias Futuras](#melhorias-futuras)
- [Autor](#autor)

---

## 🧠 Sobre o Projeto

Este programa permite **codificar e decodificar textos** com base em uma **chave de substituição**.  
Cada caractere é convertido em um número que representa sua posição dentro da chave, criando uma sequência difícil de entender sem a chave correta.

Ele também permite **gerar novas chaves aleatórias**, tornando cada codificação única.

---

## ⚙️ Como Funciona

O programa segue este fluxo:

1. O usuário escolhe no menu se quer **codificar** ou **decifrar**.
2. O texto é transformado em uma lista de números (cada caractere é convertido em seu índice na chave).
3. A lista pode ser copiada, salva ou transmitida.
4. Para decifrar, basta colar a lista novamente no programa e ele reconstrói o texto original.

A codificação é baseada em **substituição simples** (monoalfabética) — ou seja, a correspondência entre caracteres e índices é sempre a mesma para uma dada chave.

---
## 📸 Exemplos de Telas

### Menu Inicial
```
=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                                          Codificador de Texto
=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Escolha uma opção:
1 - Codificar
2 - Decifrar
3 - Gerar Chave
0 - Sair
Opção:
```



---

### Tela de Codificação
```
=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                                          Codificador de Texto
=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Digite seu texto (pressione Enter para nova linha, digite FIM para terminar):
hello world
fim

Texto encriptado
[21, 48, 83, 83, 43, 16, 9, 43, 20, 83, 18]

Pressione Enter para voltar ao menu...
```



---

### Tela com texto Decifrado
```
=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                                          Codificador de Texto
=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Digite o texto para Decifrar:
[21, 48, 83, 83, 43, 16, 9, 43, 20, 83, 18]

Texto Decifrado
hello world

Pressione Enter para voltar ao menu...
```
### Tela de Geraçcão de Chave
```
=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                                          Codificador de Texto
=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Gerando nova chave...
XOpô)YNbUIf,-S2MqdnHz'Át9áéÉú?çíaZ@âr
AWiÂBÇsõT(j ÊeÓ1CÚk_Rvm6ÔxwÕ;oê.5QÃãEÍóD0J!V3KF4lgL:7h8GcPuy

Pressione Enter para voltar ao menu...
```


## 💻 Como Executar

### 1️⃣ Pré-requisitos
- Python 3.8 ou superior instalado  
- Sistema operacional: Windows
- Opcional: `python-dotenv` se quiser carregar a chave de um arquivo `.env`

### 2️⃣ Executar o programa
No terminal ou prompt de comando:

python codify.py
