def solution(s):
    answer = True
    a=list(s)
    b=[]
    for i in a:
        if(i=='('):
            b.append(i)
        else:
            if(len(b)==0):
                answer=False
                break
            else:
                b.pop()
    if(len(b)!=0):
        answer=False
        # if(i=='('):
        #     try:
        #         a.remove(')')
        #     except:
        #         answer=False
        #         break
        # else:
        #     answer=False
        #     break
    return answer