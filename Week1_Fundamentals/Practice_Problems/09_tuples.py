if __name__ == '__main__':
    n = int(input())

    my_tuple = tuple(map(int, input().split()))

    print(hash(my_tuple))