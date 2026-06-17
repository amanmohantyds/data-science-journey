"""
Problem: Nested Lists
Link: https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

"""
if __name__ == '__main__':
    students=[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        
    scores=[]
    
    for student in students:
        scores.append(student[1])
    
    sorted_scores = sorted(set(scores))
    
    second_lowest_score=sorted_scores[1]
    
    names=[]
    for student in students:
        if student[1]==second_lowest_score:
            names.append(student[0])
    for name in sorted(names):
        print(name)