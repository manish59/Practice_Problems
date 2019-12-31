def fib(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def get_fib(n):
    dict_fib={}
    for i in range(n):
        if i not in dict_fib:
            dict_fib[i]=fib(i)
            print(dict_fib[i])
        else:
            print(dict_fib[i])
get_fib(10)