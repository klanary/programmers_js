from collections import deque
def solution(cacheSize, cities):
    cache=deque()
    answer=0
    for i in cities:
        i=i.lower()
        
        if i in cache:
            answer+=1
            cache.remove(i)
            cache.append(i)
        else:
            answer+=5
            cache.append(i)
            if len(cache)>cacheSize:
                cache.popleft()

    return answer