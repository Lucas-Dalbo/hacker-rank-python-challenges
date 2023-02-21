# Dado um dicionário de listas, de tamanho N, no formato:
#  { name: [grades]}

# Retorne a nota média de um estudante com 2 casas decimais.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    scores_by = student_marks[query_name]
    average = round(sum(scores_by) / len(scores_by), 3)
    
    print("{result:.2f}".format(result=average))
