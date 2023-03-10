# itertools.product
# Esse método realiza o produto cartesiano entre dois objetos iteráveis, tendo o mesmo efeito de [(x,y) for x in A for y in B].

from itertools import product

def cartesian_product(A:list, B:list):
    return list(product(A, B));
    
if __name__ == "__main__":
    listA = input().split(" ")
    listB = input().split(" ")
    
    print(*cartesian_product(listA, listB), sep=" ")
