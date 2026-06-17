"""
Problem: Incorrect Regex
Link: https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true

"""
def incorrect_regex():
    import re
    T=int(input())
    for _ in range(T):
       S=input()
       try:
        re.compile(S)
        print(True)
       except re.error:
        print(False)
incorrect_regex()