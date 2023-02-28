def door_mat(h, l):
    detail = ".|."
    text = "WELCOME"
    center = (h // 2)
    plain_mat = ["-"] * h
    
    for i in range(0, center):
        q = (2 * i) + 1
        line = (detail * q).center(l, "-")
        plain_mat[i] = line
        tail = (i * (-1)) - 1
        plain_mat[tail] = line
    else:
        line = text.center(l, "-")
        plain_mat[center] = line
    
    return "\n".join(plain_mat)
    

if __name__ == "__main__":
    try:
        N, M = input().split(" ")
        mat = door_mat(int(N), int(M))
        print(mat)
    except ValueError:
        print("Insira somente dois valores")
