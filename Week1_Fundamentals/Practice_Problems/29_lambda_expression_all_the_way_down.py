def lambda_depth(n):
    if n == 0:
        return "edabit"
    return lambda: lambda_depth(n - 1)

n = int(input("Enter n: "))

result = lambda_depth(n)

for _ in range(n):
    result = result()

print(result)