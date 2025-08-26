def solution(s):
    a=list(s)
    b=[]
    for i in a:
        if(len(b)>0):
            if(b[-1]==i):
                b.pop()
                continue
        b.append(i)
    if(len(b)>0):
        return 0
    else:
        return 1
            