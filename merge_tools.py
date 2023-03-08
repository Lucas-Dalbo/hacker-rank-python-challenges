# Objetivo
# Dada um string de tamanho N, e um inteiro K, tal que K é divisor de K.
# Desenvolva uma função que divida a string em substrings de tamanho K, e as imprima no console, evitando a repetição de caracteres e mantendo a ordem de aparição.

def merge_the_tools(string, k):
    index = 0
    str_length = len(string)
    
    while index < str_length:
        sub = string[index:(k + index)]
        sub = dict.fromkeys(sub)
        sub = "".join(sub)
        print(sub)
        index += (k)

# Explicação:
# Em um loop while, primeiro se separa a parte da string desejada e em seguida, se usa o método dict.fromkeys().
# O método dict.fromkeys() constroi um dict a partir das chaves fornecidas, na ordem que são fornecidas,
# como não podem haver chaves iguais, qualquer repetição de caracteres é ignorada.
# Depois, usando o método join, fazemos o join do dict gerado, que pro padrão pega as chaves dele, depois disso, basta imprimir.
