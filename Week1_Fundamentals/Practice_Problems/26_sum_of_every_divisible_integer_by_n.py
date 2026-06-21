def evenly_divisible(a, b, c):
    # Use a list comprehension to grab all numbers divisible by c, then sum them
    
    return sum(x for x in range(a, b + 1) if x % c == 0)

print(evenly_divisible(1, 10, 2))    # Output: 30 (2 + 4 + 6 + 8 + 10)