def solution(n, left, right):
    answer = []
    
        
    for k in range(left//n+1,right//n+2):
        if left//n==right//n:
            for i in range(left%n,right%n+1):
                if(i+1<k):
                    answer.append(k)
                else:
                    answer.append(i+1)
            break
        if left//n+1==k:
            for i in range(left%n,n):
                if(i+1<k):
                    answer.append(k)
                else:
                    answer.append(i+1)
        elif k==right//n+1:
            for i in range(0,right%n+1):
                if(i+1<k):
                    answer.append(k)
                else:
                    answer.append(i+1)
        else :
            for i in range (0,n):
                if(i+1<k):
                    answer.append(k)
                else:
                    answer.append(i+1)
    
    return answer