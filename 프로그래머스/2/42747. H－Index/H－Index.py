def solution(citations):
    citations.sort(reverse=True)
    a=citations[0]
    for i in range(len(citations),0,-1):
        x= sum(1 for k in citations if k>=i)
        if x>=i:
            answer=i
            return answer
    return 0