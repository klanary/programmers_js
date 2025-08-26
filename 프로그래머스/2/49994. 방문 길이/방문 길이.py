def solution(dirs):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    last=[]
    command=[]
    for i in dirs:
        if i=='L':
            command.append(0)
        elif i=='R':
            command.append(1)
        elif i=='D':
            command.append(2)
        elif i=='U':
            command.append(3)
    cur=[0,0]
    for i in command:
        if cur[0]+dx[i]>5 or cur[0]+dx[i]<-5 or cur[1]+dy[i]>5 or cur[1]+dy[i]<-5:
            continue
        if i==0:
            path=(cur[0]+dx[i],cur[1],cur[0],cur[1]+dy[i])
        elif i==1:
            path=(cur[0],cur[1],cur[0]+dx[i],cur[1]+dy[i])
        elif i==2:
            path=(cur[0],cur[1]+dy[i],cur[0]+dx[i],cur[1])
        elif i==3:
            path=(cur[0],cur[1],cur[0]+dx[i],cur[1]+dy[i])
        last.append(path)
        cur[0]+=dx[i]
        cur[1]+=dy[i]
    answer=set(last)
    return len(answer)