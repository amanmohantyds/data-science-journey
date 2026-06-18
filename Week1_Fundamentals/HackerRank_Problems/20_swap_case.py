"""
Problem: Swap Case
Link: https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

"""
def swap_case(s):
    l=s.swapcase()
    return l

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result) 