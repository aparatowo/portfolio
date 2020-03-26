def fibo(a=0, b=1):
    first_one = a
    second_one = b
    while True:
        fibo = first_one
        yield fibo
        first_one = second_one
        second_one += fibo

def fibonacci(a=0, b=1):
    yield a
    yield b
    while True:
        yield a + b
        a, b = b, a + b


if __name__ == '__main__':
    f = fibo()
    ff = fibonacci()

    for _ in range(10):
        print(next(f))
    print('Wyszedłem z pętli 10')
    print('I kolejny ciąg...')
    for _ in range(10):
        print(next(ff))
    print('Wyszedłem z pętli 10')
    print(next(f))
    print(next(ff))
