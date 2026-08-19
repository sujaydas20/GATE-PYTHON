def fun(n):
    if n>0:
     print(n)
     fun (n-1)
     print(n)

fun( 5)













def fun(n):
    if n > 0:
        print(n, end="")
        fun(n-1)
        print(n, end="")

fun(3)








a = [1, 2, 3]
b = a
b[0] = 10

print(a)








def fun(n):
    if n == 0:
        return 0
    return n + fun(n-1)

print(fun(4))