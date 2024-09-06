const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

class Queue {
  constructor() {
    this.items = [];
    this.front = 0;
    this.rear = 0;
  }

  enqueue(element) {
    this.items.push(element);
    this.rear += 1;
  }

  dequeue() {
    return this.items[this.front++];
  }

  front() {
    return this.items[front];
  }

  isEmpty() {
    return this.front === this.rear;
  }

  size() {
    return this.rear - this.front;
  }
}

const input = [];
let currentLine = 0;

rl.on("line", (line) => {
  input.push(line.split(" ").map(Number));
});

rl.on("close", () => {
  const [M, N] = input[currentLine]; // M은 가로길이, N은 세로 길이

  const box = Array.from({ length: N }, () => []);

  for (let n = 0; n < N; n++) {
    currentLine += 1;
    for (let m = 0; m < M; m++) {
      box[n].push(input[currentLine][m]);
    }
  }

  const dirs = [1, -1, 0, 0, 1, -1];
  const bfs = (maturedPositions) => {
    const q = new Queue();

    for (const matured of maturedPositions) {
      q.enqueue(matured);
    }

    while (q.size() > 0) {
      [y, x] = q.dequeue();
      let day = box[y][x];

      for (let k = 0; k < 4; k++) {
        newY = y + dirs[k];
        newX = x + dirs[k + 2];
        if (
          newY < 0 ||
          newX < 0 ||
          newY >= N ||
          newX >= M ||
          box[newY][newX] !== 0
        ) {
          continue;
        }
        q.enqueue([newY, newX]);
        box[newY][newX] = day + 1;
      }
    }
  };

  const maturedPositions = [];
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (box[i][j] === 1) {
        maturedPositions.push([i, j]);
      }
    }
  }
  bfs(maturedPositions);

  const getDays = () => {
    let max = -Infinity;
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < M; j++) {
        if (box[i][j] === 0) {
          return -1;
        }

        if (box[i][j] > max) {
          max = box[i][j];
        }
      }
    }

    return max - 1;
  };

  console.log(getDays());
  process.exit();
});
