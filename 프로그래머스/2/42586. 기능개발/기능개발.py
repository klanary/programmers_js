def solution(progresses, speeds):
    answer = []
    day=0
    for i in range(len(progresses)):
        if progresses[i]+day*speeds[i]>=100:
            answer[-1]+=1
            continue
        else:
            while progresses[i]+day*speeds[i]<100:
                day+=1
            answer.append(1)
    return answer