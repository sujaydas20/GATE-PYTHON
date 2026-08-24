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



















def fun(n):
    if n <= 1:
        return n
    return fun(n-1) + n

print(fun(5))






def fun(n):
    if n <= 1:
        return 1
    return fun(n-1) + fun(n-2)

print(fun(5))








def fun(n):
    if n == 0:
        return
    if n % 2 == 0:
        print(n, end=" ")
    fun(n-1)

fun(6)





def fun(n):
    if n <= 1:
        return
    fun(n-1)
    fun(n-1)

fun(6)






def fun(n):
    if n == 0:
        return
    print(n, end=" ")
    fun(n - 1)

fun(5)







def fun(n):
    if n == 0:
        return
    fun(n - 1)
    print(n, end=" ")

fun(4)







def fun(n):
    if n == 0:
        return
    print(n, end=" ")
    fun(n - 1)
    print(n, end=" ")

fun(3)




def fun(n):
    if n == 1:
        return 1
    return n + fun(n - 1)

print(fun(5))


def fun(n):
    if n <= 1:
        return 1
    return fun(n - 1) + fun(n - 2)

print(fun(5))