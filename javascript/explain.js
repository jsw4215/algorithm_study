let s = "try hello world"

function solution(s) {
  let answer = "";

  let str = s.split(" ");
  console.log(str)

  for (let i = 0; i < str.length; i++) {
    for (let j = 0; j < str[i].length; j++) {
      if (j % 2 ==0) {
        answer += str[i][j].toUpperCase();
      } else {
        answer += str[i][j].toLowerCase();
      }
    }
    if (i < str.length -1) {
      answer = answer + " ";
    }
  }
  return answer
}
console.log(solution(s))