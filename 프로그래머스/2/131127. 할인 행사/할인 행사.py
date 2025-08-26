def solution(want, number, discount):
    diction=dict(zip(want,number))
    count=0
    for i in range(0,len(discount)-9):
        a=sorted(discount[i:i+10])
        b=set()
        j=0
        while j<10:
            c=a.count(a[j])
            z=(a[j],c)
            b.add(z)
            j+=c
        d=dict(b)
        if(diction==d):
            count+=1
    return count
        
        
        
            
        