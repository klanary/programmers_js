def solution(arr1, arr2):
    answer=[]    
    answer=[]

    for j in range(0,len(arr1)):
        result=[]
        for k in range(0,len(arr2[0])):
            a=0
            for i in range(0,len(arr1[0])):
                a+=arr1[j][i]*arr2[i][k]
            result.append(a)
        answer.append(result)
    
    return answer