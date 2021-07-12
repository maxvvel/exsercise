# написати функцію, яка буде знаходити факторіал числа.
def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n


n = int(input("введіть число: "))
print(fac(n))
