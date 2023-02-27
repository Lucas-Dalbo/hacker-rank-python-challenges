def count_substring(string, sub_string):
    try:
        result = string.index(sub_string)
        new_string = string[result + 1:]
        return 1 + count_substring(new_string, sub_string)
    except ValueError:
        return 0


if __name__ == '__main__':
    string = input("Digite uma string: ").strip()
    sub_string = input("Digite outra string: ").strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
