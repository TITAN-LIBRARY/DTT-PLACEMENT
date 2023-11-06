# Recursive function

def fun(n):
    if n != 0:
        fun(n-1)
        print(n)
        fun(n-1)


n = int(input())
fun(n)
