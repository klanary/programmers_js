def solution(order):
    container=[]
    j=0
    i=0
    while i<len(order)+1:
        if j==len(order):
            break
        if len(container)>0:
            if container[-1]==order[j]:
                container.pop()
                j+=1         
                continue
        i+=1
        if i==order[j]:
            j+=1
            continue
        container.append(i)
    return j