def Max(list):
    print(list)
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
        print(m)
        if m > list[0]:
            return m
        else:
            return list[0]

def main():
    list = [1,2,8,4,5,6,7,6]
    print("the largest number is: ", Max(list))

main()