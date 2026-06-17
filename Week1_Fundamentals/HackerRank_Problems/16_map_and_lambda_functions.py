"""
Problem: Map and Lambda Functions
Link: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true

"""
cube = lambda x: x**3

def fibonacci(n):
    fib = []
    a, b = 0, 1

    for _ in range(n):
        fib.append(a)
        a, b = b, a + b

    return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

#IMP  