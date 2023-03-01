const caseA = {
 people: [70, 50, 80, 50],
 limit: 100,
};

const caseB = {
 people: [70, 80, 50],
 limit: 100,
};

function solution(people, limit) {
 let answer = 0;

 const arrangedPeople = people.sort((a, b) => b - a);
 console.log("check", arrangedPeople);

 let start = 0;
 let end = arrangedPeople.length - 1;
 while (start <= end) {
  let heavyPerson = arrangedPeople[start];
  let lightPerson = arrangedPeople[end];

  if (lightPerson + heavyPerson <= limit) {
   end -= 1;
  }
  // 무거운 사람을 태워버림**
  start += 1;
  answer += 1;
 }

 return answer;
}

console.log(solution(caseA.people, caseA.limit));
