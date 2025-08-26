from collections import Counter
import math

def solution(str1, str2):
    # 두 글자로 구성된 원소들을 추출
    set_str1 = []
    set_str2 = []
    
    # str1 처리
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            set_str1.append(str1[i].lower() + str1[i+1].lower())
            
    # str2 처리
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            set_str2.append(str2[i].lower() + str2[i+1].lower())
    
    # 다중집합(multiset) 처리를 위해 Counter 사용
    counter1 = Counter(set_str1)
    counter2 = Counter(set_str2)
    
    # 교집합: 각 원소별로 최솟값을 취함
    intersection = sum((counter1 & counter2).values())
    
    # 합집합: 각 원소별로 최댓값을 취함
    union = sum((counter1 | counter2).values())
    
    # 공집합인 경우
    if union == 0:
        return 65536
    
    # 자카드 유사도 계산
    jaccard = intersection / union
    return math.floor(65536 * jaccard)
