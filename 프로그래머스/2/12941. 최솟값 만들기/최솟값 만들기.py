def solution(A,B):
    sum =0
    a=len(A)
    A.sort()
    B.sort()
    for i in range(0,a):
        sum+=A[i]*B[a-1-i]
    return sum