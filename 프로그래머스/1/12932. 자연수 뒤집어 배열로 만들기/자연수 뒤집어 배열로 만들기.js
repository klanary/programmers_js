function solution(n) {
    var answer = String(n).split('').map(Number);
    answer = answer.reverse();
    return answer;
}