def solution(s):
    answer=0
    result=0
    for i in range(0,len(s)):
        x=list(s[i:]+s[0:i])
        k=[]
        for j in range(len(x),0,-1):
            y=x.pop()
            
            if(y == ')'or y==']' or y=='}'):
                k.append(y)
            elif(y=='('):
                if(len(k)>0):
                    a=k.pop()
                else:
                    break
                if(a!=')'):
                    break
            elif(y=='['):
                if(len(k)>0):
                    a=k.pop()
                else:
                    break
                if(a!=']'):
                    break
            elif(y=='{'):
                if(len(k)>0):
                    a=k.pop()
                else:
                    break
                if(a!='}'):
                    break
            
            if(len(x)==0 and len(k)==0):
                result+=1
            
    return result
            
        