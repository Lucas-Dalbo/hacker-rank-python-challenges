# Dado um valor N, imprima os valores no formato 123...N.
# Exemplo:
#   n = 5
#   saida = 12345

if __name__ == '__main__':
    n = int(input())
    i = range(1, n + 1)
    print(*i, sep="")
