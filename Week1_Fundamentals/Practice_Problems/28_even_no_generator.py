def find_even_nums(num):
    return [n for n in range(2,num+1) if n % 2 == 0]

# Get input, convert it to an integer, and print the result
user_num = int(input("Enter a number: "))
print(find_even_nums(user_num))