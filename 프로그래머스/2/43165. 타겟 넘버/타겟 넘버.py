from itertools import combinations
def solution(numbers, target):
    answer = sum(numbers)
    count=0
    for i in range(len(numbers)):
        k=list(combinations(numbers,i))#리스트안튜플
        for j in k:#튜플추출
            result=answer-2*sum(j)
            if result==target:
                count+=1
    return count