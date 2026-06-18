if __name__ == '__main__':
    print("Enter number of scores:")
    n = int(input())
    print("Enter scores")
    arr = map(int, input().split())
    scores= list(arr)
    print("runner up score is:",sorted(set(scores))[-2])
