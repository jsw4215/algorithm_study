const caseA = {
 numbers: "1 2 3 4",
};

function solution(s) {
 var answer = 0;

 const sArr = s.split(" ").map((str) => Number(str));

 return `${Math.min(...sArr)} ${Math.max(...sArr)}`;
}

console.log("check", solution(caseA.numbers));
