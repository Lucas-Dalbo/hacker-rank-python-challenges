# Objetivo:
# Definir uma função que calcula quantas substrings existem em uma string e determinar a pontuação baseada em quantas começam com vogais e quantas começam não.
# Kevin ganha ponto quando começa com vogal, Stuart ganha quando começa com consoante.

def minion_game(string: str):
    string = string.lower()
    vowels = "aeiou"
    kevin, stuart = 0, 0
    length = len(string)
    
    for i in range(length):
        if string[i] in vowels:
            kevin += length - i
        else:
            stuart += length - i
    
    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif kevin < stuart:
        print(f"Stuart {stuart}")
    else:
        print("Draw")

# Explicação:
# Não é preciso saber como a substring se parece, somente a quantidade delas.
# Por exemplo, em uma palavra com 4 letras, se pegarmos substrings que começam com a primeira letra, o máximo serão 4 substrings, a partir da segunda letra 3, e assim por diante.
# STRING: CASA
# SUBSSTRINGS QUE COMEÇAM COM "C": CASA, CAS, CA, C
# Logo a pontuação acontece calculando (tamanho original da string - o indice atual), e basta saber se a primeira letra da substring é vogal ou consoante, para atribuir os pontos.
