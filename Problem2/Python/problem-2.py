def Fibonacci(number):
    a, b = 0,1
    while a <= number:
        yield a
        a,b = b, a+b

def generate_sum(number):
    return sum([i for i in Fibonacci(number) if i % 2 == 0])

print(generate_sum(4000000))
