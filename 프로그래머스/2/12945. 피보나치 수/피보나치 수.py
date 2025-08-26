def solution(n):
    piv=[0,1]
    for i in range(2,n+1,1):
        piv.append(piv[i-2]+piv[i-1])
    return (piv[n]%1234567)