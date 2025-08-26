def solution(clothes):
    x= set()
    answer=1
    for i in range(0,len(clothes)):
        x.add(clothes[i][1])
    z=list(x)
    y=[1]*len(z)
    
    for j in range(0,len(clothes)):
        y[z.index(clothes[j][1])]+=1
    
    for m in y:
        answer*=m
                
        
    return answer-1