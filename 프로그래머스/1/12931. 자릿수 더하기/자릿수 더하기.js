function solution(n)
{
    var answer = 0;
    for(let i=1;i<=n;i*=10){
        answer+=Math.floor((n/i))%10
    }
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    console.log(answer)

    return answer;
}