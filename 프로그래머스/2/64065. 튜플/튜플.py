from collections import Counter
def solution(s):
    answer = []
    l=s.replace('{',"")
    l=l.replace('}',"")
    l=l.split(",")
    x=Counter(l)
    for i,j in x.most_common():
        answer.append(int(i))
    return answer