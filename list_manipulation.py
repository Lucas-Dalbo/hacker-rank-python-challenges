# Dado um lista de tamanho N, com ccada valor de N sendo um comando para manipular a lista de inteiros my_list.
# Implemente o código para que seja possivel executar os métodos de lista, a partir dos comandos.

if __name__ == '__main__':
    N = int(input())
    my_list = list()

    def insert(lista, i, e):
        lista.insert(i, e)
    
    def remove(lista, e, *i):
        lista.remove(e)
    
    def append(lista, e, *i):
        lista.append(e)
    
    def sort(lista, *i):
        lista.sort()
    
    def pop(lista, *i):
        lista.pop()
    
    def reverse(lista, *i):
        lista.reverse()
    
    def print_list(lista, *i):
        print(lista)
    
    commands = {
        "insert": insert,
        "print": print_list,
        "remove": remove,
        "append": append,
        "sort": sort,
        "pop": pop,
        "reverse": reverse,
    }
    
    for i in range(0, N):
        cmm_input = input()
        cmm_list = cmm_input.split()
        
        if len(cmm_list) < 3:
            cmm_list.extend([False] * (3 - len(cmm_list)))
        
        cmm, el, id = cmm_list
        commands[cmm](my_list, int(el), int(id))
        
