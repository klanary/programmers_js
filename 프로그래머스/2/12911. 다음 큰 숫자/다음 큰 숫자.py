def solution(n):
    x=n+1
    while True:
        if str(bin(n)).count(str(1))==str(bin(x)).count(str(1)):
            break
        x+=1
    return x