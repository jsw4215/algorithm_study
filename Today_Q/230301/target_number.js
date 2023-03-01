const caseA = {
 numbers: [4, 1, 2, 1],
 target: 2,
};

function solution(numbers, target) {
 var answer = 0;

 const dfs = (level, sum) => {
  if (level === numbers.length) {
   if (sum === target) {
    answer += 1;
   }
   return;
  }

  dfs(level + 1, sum + numbers[level]);
  dfs(level + 1, sum - numbers[level]);
 };

 dfs(0, 0);

 return answer;
}

console.log("check", solution(caseA.numbers, caseA.target));
