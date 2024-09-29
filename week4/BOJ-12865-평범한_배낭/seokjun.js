// 실패!
// N개 물건 주어짐.
// 긱 물건의 무게 w, 가치 v 주어짐.
// 물건 합해서 무게 K 이하, 가치 최대했을 때, 가치의 최댓값 반환
// dp[i] = 무게 i일 때 최대 가치
// 어떤 물건을 넣었는지, 그떄 최대 무게는 뭔지 정보가 있어야함.
// dp[i-1] = 무게 i-1일 때 최대 가치
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

rl.on("line", (line) => {
  input.push(line);
});

rl.on("close", () => {
  const [N, K] = input[0].split(" ").map(Number);
  const items = [];

  for (let i = 0; i < N; i++) {
    const [w, v] = input[i + 1].split(" ").map(Number);
    items.push([w, v]);
  }

  sorted = items.sort((item1, item2) => {
    const [w1, v1] = item1;
    const [w2, v2] = item2;
    return w1 - w2;
  });

  console.log(sorted);
  process.exit();
});
