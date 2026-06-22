def num_args(*args):
    return len(args)

args = input("Enter values separated by space: ").split()

print(num_args(*args))