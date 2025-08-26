def solution(numbers):
    answer = [-1] * len(numbers)  # 기본 -1로 초기화
    stack = []  # 아직 다음 큰 수를 찾지 못한 인덱스 저장
    
    for i, num in enumerate(numbers):
        # 스택의 top이 현재 값보다 작으면 현재 값이 "다음 큰 수"
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(i)

    return answer
