# Dada oos valores X,Y,Z e N, imprima uma lista result, onde cada elemento de result é uma lista [I, J, K].
# Tal que:
#   0 <= I <= X
#   0 <= J <= Y
#   0 <= K <= Z
#   e I + J + K é diferente de N.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = [[i, j, k] for i in range(0, x + 1)
                        for j in range(0, y + 1)
                        for k in range(0, z + 1)
                        if i + j + k != n]
    
    print(result)
