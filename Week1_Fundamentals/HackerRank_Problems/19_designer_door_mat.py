"""
Problem: Designer Door Mat
Link: https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true

"""
def designer_door_mat():
 if __name__ == '__main__':
    
    N,M=map(int,input().split())
    
    # Top half
    for i in range(1,N,2):
        print((".|.*" * i).center(M, "-"))
        
    # Middle    
    print("WELCOME".center(M, "-"))
    
    # Bottom half
    for i in range(N-2,0,-2):
        print((".|.*" * i).center(M,"-")) 
designer_door_mat()           