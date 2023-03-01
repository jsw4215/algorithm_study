class MinHeap {
 constructor() {
  this.heap = [null];
 }

 size() {
  return this.heap.length - 1;
 }

 getMin() {
  return this.heap[1] ? this.heap[1] : null;
 }

 swap(a, b) {
  [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
 }

 heappush(value) {
  this.heap.push(value);
  let curIdx = this.heap.length - 1;
  let parIdx = (curIdx / 2) >> 0;

  while (curIdx > 1 && this.heap[parIdx] > this.heap[curIdx]) {
   this.swap(parIdx, curIdx);
   curIdx = parIdx;
   parIdx = (curIdx / 2) >> 0;
  }
 }

 heappop() {
  const min = this.heap[1];
  if (this.heap.length <= 2) this.heap = [null];
  else this.heap[1] = this.heap.pop();

  let curIdx = 1;
  let leftIdx = curIdx * 2;
  let rightIdx = curIdx * 2 + 1;

  if (!this.heap[leftIdx]) return min;
  if (!this.heap[rightIdx]) {
   if (this.heap[leftIdx] < this.heap[curIdx]) {
    this.swap(leftIdx, curIdx);
   }
   return min;
  }

  while (
   this.heap[leftIdx] < this.heap[curIdx] ||
   this.heap[rightIdx] < this.heap[curIdx]
  ) {
   const minIdx = this.heap[leftIdx] > this.heap[rightIdx] ? rightIdx : leftIdx;
   this.swap(minIdx, curIdx);
   curIdx = minIdx;
   leftIdx = curIdx * 2;
   rightIdx = curIdx * 2 + 1;
  }

  return min;
 }
}

const caseA = {
 people: [70, 50, 80, 50],
 limit: 100,
};

const caseB = {
 people: [70, 80, 50],
 limit: 100,
};

function solution(people, limit) {
 var answer = 0;

 // max, min을 찾는다
 // 선택된 사람과 더해져서 더 많은 사람을 싣고 갈 수 있는지 파악한다
 // n^2은 안됨
 // n log n 이 나와야할 것임
 // 투포인터, 완전탐색, 힙
 // 1. n log n으로 정렬한 후, 순서대로 limit를 넘지않게 사람들을 태워 보낸다.
 // 2. 정렬되지 않은 배열을 투포인터로 한명 한명 태워본다.
 // 3. 완전탐색으로 매번 탐색하며 적절한 인원을 태운다.

 // 1. 힙정렬 이용하여 힙소트 한다.

 const heapedArr = new MinHeap();

 for (let i = 0; i < people.length; i++) {
  heapedArr.heappush(people[i]);
 }

 // 2. 힙소트한 정렬에서 pop으로 한명씩 꺼내어 limit와 비교하며 싣어보낸다.
 let firstPerson = heapedArr.heappop();
 let peopleOnTheBoat = [firstPerson];
 let totalWeight = firstPerson;
 // answer++;
 while (heapedArr.heap.length > 1) {
  // 추가인원 무게를 더해보고, LIMIT보다 작으면 추가로 더 태운다.
  let additionalPerson = heapedArr.getMin();
  totalWeight += additionalPerson;

  if (totalWeight <= limit) {
   peopleOnTheBoat.push(heapedArr.heappop());
  } else {
   // 넘치면 answer ++ 해주고 인원들을 싣고 보낸다.
   // weight, peopleOnTheBoat 초기화
   answer++;
   totalWeight = 0;
   peopleOnTheBoat = [];
  }

  if (heapedArr.heap.length === 1) {
   answer++;
  }
 }

 return answer;
}

console.log(solution(caseA.people, caseA.limit));
