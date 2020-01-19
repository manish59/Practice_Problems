def check_permutations(s,t):
    if sorted(s)==sorted(t):
        return True
    return False
print(check_permutations("ansh","hsina"))