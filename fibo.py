def fibo(num) :
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
    return a

if __name__ == '__main__':
    print(fibo(4))
