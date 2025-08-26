def solution(k, dungeons):
    n=len(dungeons)
    max_count=0
    visited=[False]*len(dungeons)
    def dfs(hp,count):
        nonlocal max_count
        max_count=max(max_count,count)
        for i in range(n):
            min_r, consume=dungeons[i]
            if hp>=min_r and not visited[i]:
                visited[i]=True
                dfs(hp-consume, count+1)
                visited[i]=False
    dfs(k,0)
    return max_count
                
            
        