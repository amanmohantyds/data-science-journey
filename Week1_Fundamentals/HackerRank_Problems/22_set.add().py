"""
Problem: Set and .add()
Link: https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true

"""
def set_add():
 if __name__ == '__main__':
     N=int(input())
     countries = set()
     for _ in range(N):
         countries.add(input())
     print(len(countries))
set_add()     