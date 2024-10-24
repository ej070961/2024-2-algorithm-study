class Queue {
  items = [];
  front = 0;
  rear = 0;

  size() {
    return this.rear - this.front;
  }

  push(item) {
    this.items.push(item);
    this.rear += 1;
  }

  pop() {
    if (this.size() <= 0) return null;

    return this.items[this.front++];
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
let currentLine = 0;

rl.on("line", (line) => {
  input.push(line);
});

rl.on("close", () => {
  const N = Number(input[currentLine++]);
  const picture = Array.from({ length: N }, () => {});

  for (let n = 0; n < N; n++) {
    picture[n] = input[currentLine++].split("");
  }

  let normal = 0;
  let abnormal = 0;

  let visitedNormal = Array.from({ length: N }, () => {
    return Array.from({ length: N }, () => false);
  });

  let visitedAbnormal = Array.from({ length: N }, () => {
    return Array.from({ length: N }, () => false);
  });

  const dirs = [1, -1, 0, 0, 1, -1];
  const bfsNormal = (i, j) => {
    const q = new Queue();
    q.push([i, j]);
    visitedNormal[i][j] = true;

    while (q.size() > 0) {
      const [y, x] = q.pop();
      const currentColor = picture[y][x];
      for (let k = 0; k < 4; k++) {
        const [newY, newX] = [y + dirs[k], x + dirs[k + 2]];

        if (
          newY < 0 ||
          newX < 0 ||
          newY >= N ||
          newX >= N ||
          visitedNormal[newY][newX] ||
          currentColor !== picture[newY][newX]
        ) {
          continue;
        }

        q.push([newY, newX]);
        visitedNormal[newY][newX] = true;
      }
    }
  };

  const bfsAbnormal = (i, j) => {
    const isSameColor = (a, b) => {
      if (a === b || (a === "R" && b === "G") || (a === "G" && b === "R")) {
        return true;
      } else {
        return false;
      }
    };
    const q = new Queue();
    q.push([i, j]);
    visitedAbnormal[i][j] = true;

    while (q.size() > 0) {
      const [y, x] = q.pop();
      const currentColor = picture[y][x];
      for (let k = 0; k < 4; k++) {
        const [newY, newX] = [y + dirs[k], x + dirs[k + 2]];

        if (
          newY < 0 ||
          newX < 0 ||
          newY >= N ||
          newX >= N ||
          visitedAbnormal[newY][newX] ||
          !isSameColor(currentColor, picture[newY][newX])
        ) {
          continue;
        }

        q.push([newY, newX]);
        visitedAbnormal[newY][newX] = true;
      }
    }
  };

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (!visitedNormal[i][j]) {
        bfsNormal(i, j);
        normal += 1;
      }
    }
  }

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (!visitedAbnormal[i][j]) {
        bfsAbnormal(i, j);
        abnormal += 1;
      }
    }
  }

  console.log(`${normal} ${abnormal}`);
  process.exit();
});
