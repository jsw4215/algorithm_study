function solution(s){

    answer = 0

    for(let i=0;i<s.length;i++){
        item=parseInt(s[i])
        console.log("item",item)
        if(!answer||item<2){
            answer+=item
        }else{
            answer*=item
        }
    }

    console.log("ee", answer)

    return answer

}

console.log(solution("567"))