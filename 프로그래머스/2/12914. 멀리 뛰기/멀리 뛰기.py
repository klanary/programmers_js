import math
def solution(n):
    answer = 0
    for i in range(0,math.floor(n/2)+1,1):
        a=(n-2*i+1)
        answer+=math.comb(a+i-1,i)
    return answer%1234567