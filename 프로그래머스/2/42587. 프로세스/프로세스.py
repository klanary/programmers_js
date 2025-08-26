from collections import deque
def solution(priorities, location):
    a=deque()
    cnt=0
    for i in range(len(priorities)):
        if(i==location):
            a.append([priorities[i],True])
        else:
            a.append([priorities[i],False])
    
    while len(a)>0:
        
        if(a[0][0]!=max(map(lambda x: x[0],a))):
            k=a.popleft()
            a.append(k)
        else:
            k=a.popleft()
            cnt+=1
            if(k[1]==True):
                return cnt
        