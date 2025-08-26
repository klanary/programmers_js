def solution(word):
    answer = 0
    weight=[781,156,31,6,1]
    alpha=['A','E','I','O','U']
    for i in range(len(word)):
        num=alpha.index(word[i])
        answer+=weight[i]*num
    answer+=len(word)
    return answer