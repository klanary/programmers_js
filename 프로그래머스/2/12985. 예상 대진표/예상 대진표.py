def solution(n,a,b):
    answer = 0
    a-=1
    b-=1#0,1,2,3,4,5,6,7,...
    i=1
    while a!=b:
        i*=2
        a-=a%i
        b-=b%i
        answer+=1
    return answer