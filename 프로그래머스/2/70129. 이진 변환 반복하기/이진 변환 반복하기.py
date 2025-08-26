
def solution(s):
    a=0
    b=0
    while s!="1":
        b+=1
        a+=s.count('0')
        s=s.replace('0','')
        s=len(s)
        s=bin(s)[2:]
        s=str(s)
    return [b,a]