const dijkstra = (n, adj) => {
    const dist = Array(n + 1).fill(false);
    const queue = [];
  
    queue.push({ to: 1, cost: 0 });
    dist[1] = 0;
  
    while (queue.length !== 0) {
      let { to, cost } = queue.shift();
  
      adj[to].map((nextNode) => {
        const nextCost = cost + 1;
        if (dist[nextNode] === false) {
          dist[nextNode] = nextCost;
          queue.push({ to: nextNode, cost: nextCost });
        }
      });
    }
    console.log("dist:",dist)
    const max = Math.max(...dist);
    return dist.filter((num) => {
      return num === max;
    }).length;
  };
  
  function solution(n, edge) {
    let answer = 0;
    let adj = Array.from({ length: n + 1 }, () => []);
  
    // 인접 리스트 생성
    edge.forEach((route) => {
      adj[route[0]].push(route[1]);
      adj[route[1]].push(route[0]);
    });
  
    // 다익스트라
    answer = dijkstra(n, adj);
    return answer;
  }

console.log(solution(6, [[1,2],[2,3],[3,4],[4,5],[3,6]]))