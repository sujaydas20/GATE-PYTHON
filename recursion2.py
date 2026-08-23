def fun(n):
    if n == 0:
        return
    print(n, end=" ")
    fun(n-1)

fun(4)





def fun(n):
    if n == 0:
        return
    print(n, end=" ")
    fun(n-1)
    print(n, end=" ")

fun(3)