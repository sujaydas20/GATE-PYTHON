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