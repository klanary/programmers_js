def solution(n, t, m, p):
#     n진수
    answer = '0'
    num_list=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    
    position=num_list[0:n]
    for i in range(0,m*t):
        k=''
        while i!=0:
            q=i%n
            i=i//n
            k=num_list[q]+k
        answer=answer+k
            
                
    return answer[p-1:m*t+p-1:m]