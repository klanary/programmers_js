import itertools
import math
def solution(numbers):
    answer = 0
    result=[]
    prime_list=set()
    for i in range(len(numbers)):
        result.append(list(itertools.permutations(numbers,i+1)))
    for j in range(len(result)):
        for k in range(len(result[j])):
            if result[j][k][0]=="0":
                a=True
            elif j==0 and result[j][k][0]=="1":
                a=True
            else:
                comb="".join(result[j][k])
                comb=int(comb)
                prime_list.add(comb)
    prime_list=list(prime_list)
    answer=len(prime_list)
    
    for i in range(len(prime_list)):
        for k in range(2,int(math.sqrt(prime_list[i]))+1):
            if prime_list[i]%k==0:
                answer-=1
                break
    return answer