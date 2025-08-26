def solution(brown, yellow):
    sum=brown+yellow
    #a*b=sum ,(a-2)  *  (b-2)=yellow  brown=2a+2b-4
    a=3
    while True:
        if sum%a==0:
            if a>=sum/a:
                if 2*(a+sum/a-2)==brown:
                    return([a,sum/a])
        a+=1