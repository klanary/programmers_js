def solution(s):
    a = s.split()
    a= list(map(int,a))
    a.sort()
    a= list(map(str,a))
    answer=a[0]+" "+a[-1]
        
    return answer