import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    result = ''
    while n > 0:
        result = str(n % k) + result
        n //= k
    
    answer = 0
    for part in result.split('0'):
        if part and is_prime(int(part)):
            answer += 1
    return answer
