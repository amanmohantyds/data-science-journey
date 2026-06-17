"""
Problem: Exceptions
Link: https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true

"""
def exceptions():
 if __name__ == '__main__':
     N = int(input())

     for _ in range(N):
        a, b = input().split()

        try:
            print(int(a) // int(b))
        except ZeroDivisionError as e:
            print("Error Code:", e)
        except ValueError as e:
            print("Error Code:", e)
exceptions()     