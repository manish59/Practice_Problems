def is_unique(var):
    a=[]
    for i in var:
        if i not in a:
            a.append(i)
        else:
            return False
    print(a)
    return True
if __name__ == "__main__":
    print(is_unique("manish")) 