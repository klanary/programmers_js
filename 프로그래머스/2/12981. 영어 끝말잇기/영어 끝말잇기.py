def solution(n, words):
    words.reverse()
    k=[]
    turn=0
    while len(words)>0:
        i=words.pop()
        turn+=1
        if (k!=[]):
            if(i[0]!=m[-1]):
                break
        m=i
        if(k.count(m)>0):
            break
        k.append(m)
        if(len(words)==0):
            return[0,0]
            break
    return [(turn-1)%n+1,turn//n+int(turn%n>0)]