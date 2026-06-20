if __name__ ==  "__main__":
    n=int(input())
    student_mark={}
    for _ in range(n):
        name,*line=input().split()
        score=list(map(float,line))
        student_mark[name]=score
    query_name=input()
    avg= sum(student_mark[query_name])/len(student_mark[query_name])   
    print(f"{avg:.2f}")