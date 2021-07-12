#те ж саме, але без рекурсії .
n = int(input("введіть число: "))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
    print(factorial)
