def permutations(str):
    print(str)
    for i in range(len(str)):
        print(str[:i+1])
        return permutations(str[i+1:])
permutations("abc")