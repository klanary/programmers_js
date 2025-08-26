def solution(arr):
    arr.sort()
    answer=arr.pop()
    while arr!=[]:
        p=arr.pop()
        for i in range(p,0,-1):
            if(p%i==0 and answer%i==0):
                answer=answer*p/i
                break;
    return answer