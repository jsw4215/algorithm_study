function solution(people, limit) {
 let lookup = {};
 let total = 0;
 let check = false;

 for (let item of people) {
  lookup[item] = (lookup[item] || 0) + 1;
 }

 for (let i = 0; i < people.length; i++) {
  let item = people[i];
  check = false;

  lookup[item] -= 1;

  for (key in lookup) {
   if (lookup[key] >= 1) {
    if (Number(item) + Number(key) <= Number(limit)) {
     lookup[key] -= 1;
     total += 1;
     check = true;
    }
   }
  }

  if (check == false) {
   lookup[item] += 1;
  }
 }

 for (key in lookup) {
  if (lookup[key] >= 1) {
   total += lookup[key];
  }
 }

 return total;
}

console.log(solution([70, 50, 80, 50], 100)); // 3
console.log(solution([70, 80, 50], 100)); // 3
