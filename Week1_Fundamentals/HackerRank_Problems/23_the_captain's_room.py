if __name__=="__main__":
    K=int(input())
    rooms=list(map(int,input().split()))
    captain_room=(K*sum(set(rooms))-sum(rooms))//(K-1)
    print(captain_room)