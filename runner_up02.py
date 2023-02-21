# Dada uma lista students de listas [name, score]
# Encontre o nome do estudante(s), que possui a segunda menor nota da classe, exiba os nomes em ordem alfabetica.

if __name__ == '__main__':
    students = []
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.add(score)
    
    students.sort(key=lambda x: x[0])
    
    second_lowest = sorted(list(scores))[1]
    
    for name, grade in students:
        if grade == second_lowest:
            print(name)
