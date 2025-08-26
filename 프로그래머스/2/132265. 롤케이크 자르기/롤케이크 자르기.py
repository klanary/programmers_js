from collections import Counter
def solution(topping):
    answer = 0
    s=set()
    counts=Counter(topping)
    for i in range(len(topping)-1,0,-1):
        
        k=topping.pop()
        s.add(k)
        counts[k]-=1
        if(counts[k]==0):
            del counts[k]
        if len(counts)==len(s):
            answer+=1
        
    return answer