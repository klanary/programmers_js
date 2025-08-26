from collections import deque
def solution(maps):
    rest=deque()
    rest.append([0,0,1])
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    m=len(maps)
    n=len(maps[0])
    while True: #rest[0][0]!=m-1 or rest[0][1]!=n-1
        cur=rest.popleft()
        y=cur[0]
        x=cur[1]
        time=cur[2]+1
        maps[y][x]=0
        for i in range(4):
            RX=x+dx[i]
            RY=y+dy[i]
            if(RX>=0 and RX<n and RY>=0 and RY<m):
                if(maps[RY][RX]==1):
                    if([RY,RX]==[m-1,n-1]):
                        return time
                    rest.append([RY,RX,time])
                    maps[RY][RX]=0
                    
        if(len(rest)==0):
            return -1
#     answer=rest.popleft()       
                        
        
#     return answer[2]