def solution(msg):
    answer = []
    LZW=dict()
    for i in range(1,27):
        LZW[chr(i+64)]=i
    j=0
    k=27
    a=""
    while j<len(msg):
        
        a=a+msg[j]
        j+=1
        
        if a in LZW.keys():
            
            b=a
            if j==len(msg):
                answer.append(LZW[b])
            else:
                
                continue
        else:
            LZW[a]=k
            a=""
            j-=1
            k+=1
            answer.append(LZW[b])
    return answer