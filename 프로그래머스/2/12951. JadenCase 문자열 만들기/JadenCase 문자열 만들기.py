import re
def solution(s):
    answer=re.sub(r"\S+",lambda k:k.group(0)[0].upper()+k.group(0)[1:],s.lower())
    return answer