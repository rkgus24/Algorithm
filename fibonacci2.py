def f(n):
    a, b = 1, 1
    for i in range(n - 2):
        a, b = b, a + b
    return b

def fibo(n):
    return n - 2

s = int(input())

print(f"{f(s)} {fibo(s)}")
