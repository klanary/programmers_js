from collections import Counter
def solution(k, tangerine):
    count=Counter(tangerine)
    count_arr=sorted(count.items(),key=lambda item:item[1],reverse=True)
    sum=0
    for i in range(0,len(count_arr),1):
        result=i
        if(sum>=k):
            return result
            break
        else:
            sum+=count_arr[i][1]
    return len(count_arr)