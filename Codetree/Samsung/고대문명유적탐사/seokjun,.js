/*
5x5 유적지, 각 칸은 7종류의 서로 유물 조각으로 이뤄짐.
1. 탐사 진행
- 3x3 격자 선택 후, 90도만큼 1~3번 회전
- 가능한 회전 방법 중 다음 조건을 만족시키는 방법 선택. 앞의 조건을 만족시키는 방법이 다수면, 그 다음 조건으로 넘어감.
a) 1차 유물 획득 가치 최대
b) 회전 각도 최소
c) 격자 중심의 열이 가장 작음
d) 격자 중심의 행이 가장 작음

2. 1차 유물 획득
- 인접한 같은 종류의 유물 조각이 3개 이상 연결된 경우 조각이 유물이 됨.
- 유물이 된 조각들은 사라지고, 그 가치는 조각의 개수와 같음.
- 유물 조각이 사라진 칸은 다음 방법에 따라 새 조각으로 채워짐.
  - 유적 벽면에 적힌 숫자 순서대로 빈 칸을 채움.
  - 채우는 순서: 열 번호가 작은 순, 열 번호가 같다면 행번호가 큰 순. (하->상, 좌->우)

3. 유물 연쇄 획득
- 1차 유물 획득 이후, 인접한 같은 종류의 유물 조각이 3개 이상 연결된 경우 조각이 유물이 됨.
- 유물이 된 조각들은 사라지고, 그 가치는 조각의 개수와 같음.
- 유물 조각이 사라진 칸은 다음 방법에 따라 새 조각으로 채워짐.
  - 유적 벽면에 적힌 숫자 순서대로 빈 칸을 채움.
  - 채우는 순서: 열 번호가 작은 순, 열 번호가 같다면 행번호가 큰 순. (하->상, 좌->우)

1~3 과정은 1턴으로 봄.
K턴을 진행하되, 유물 1개도 획득하는 방법이 없으면, 턴이 남더라도 종료함.
*/

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

class Queue {
  constructor(items) {
    this.items = items;
    this.front = 0;
    this.rear = items.length;
  }

  size() {
    return this.rear - this.front;
  }

  push(item) {
    this.items.push(item);
    this.rear += 1;
  }

  pop() {
    if (this.size() === 0) {
      return null;
    }

    return this.items[this.front++];
  }

  toArray() {
    return this.items.slice(this.front, this.rear);
  }
}

const input = [];

rl.on("line", (line) => input.push(line));

/*
유적지 생성
1~K턴 반복
  이번 턴에 획득할 유물 가치 담을 변수 설정
  탐사 진행
  - 격자를 선택하고, 회전하고, 완성 가능한 유물의 총 가치 구함.
  - 모든 방법의 유물 가치가 0이라면, 턴 종료.
  - 그렇지 않다면 a~d 순서에 따라 방법을 선택

  1차 획득
  - 유물 가치를 저장함
  - 빈 칸 뚫음
  - 빈 칸에 벽면 유물 채움.(유적지 칸에 사용된 벽면 유물은 벽면에서 제거)

  유물 획득 가능한지 확인하고, 가능하다면 아래 반복
    - 유물 가치를 저장함
    - 빈 칸 뚫음
    - 빈 칸에 벽면 유물 채움.(유적지 칸에 사영된 벽면 유물은 벽면에서 제거)
*/

rl.on("close", () => {
  const [K, M] = input[0].split(" ").map(Number);
  const board = [];
  for (let i = 1; i <= 5; i++) {
    board.push(input[i].split(" ").map(Number));
  }
  const wall = new Queue(input[6].split(" ").map(Number));
  let totalValues = [];

  function getCandidateBoard(y, x, angle) {
    const copied = board.map((innerArray) => [...innerArray]);
    const yStart = y - 1;
    const xStart = x - 1;
    const grid = Array.from({ length: 3 }, () => Array(3).fill(0));

    for (let i = yStart; i < yStart + 3; i++) {
      for (let j = xStart; j < xStart + 3; j++) {
        grid[i - yStart][j - xStart] = board[i][j];
      }
    }

    switch (angle) {
      case 0:
        for (let i = 0; i < 3; i++) {
          for (let j = 0; j < 3; j++) {
            copied[j + yStart][2 - i + xStart] = grid[i][j];
          }
        }
        break;
      case 1:
        for (let i = 0; i < 3; i++) {
          for (let j = 0; j < 3; j++) {
            copied[2 - i + yStart][2 - j + xStart] = grid[i][j];
          }
        }
        break;
      case 2:
        for (let i = 0; i < 3; i++) {
          for (let j = 0; j < 3; j++) {
            copied[2 - j + yStart][i + xStart] = grid[i][j];
          }
        }
        break;
    }

    // 디버깅
    // console.log(`x: ${x}, y: ${y}, angle: ${angle * 90 + 90}`);
    // console.log(copied);

    return copied;
  }

  const yDirs = [-1, 0, 1, 0];
  const xDirs = [0, 1, 0, -1];
  function getCandidateValue(candidateBoard) {
    const visited = Array.from({ length: 5 }, () => Array(5).fill(false));
    let candidateValue = 0;

    for (let i = 0; i < 5; i++) {
      for (let j = 0; j < 5; j++) {
        if (visited[i][j]) {
          continue;
        }

        const q = new Queue([]);
        q.push([i, j]);
        visited[i][j] = true;
        let cnt = 0;

        while (q.size() > 0) {
          const [curY, curX] = q.pop();
          cnt += 1;
          const curPiece = candidateBoard[curY][curX];

          for (let d = 0; d < 4; d++) {
            const [newY, newX] = [curY + yDirs[d], curX + xDirs[d]];

            if (newY < 0 || newY >= 5 || newX < 0 || newX >= 5) {
              continue;
            }

            if (visited[newY][newX]) {
              continue;
            }

            if (candidateBoard[newY][newX] === curPiece) {
              q.push([newY, newX]);
              visited[newY][newX] = true;
            }
          }
        }
        if (cnt >= 3) {
          candidateValue += cnt;
        }
      }
    }
    // 디버깅
    // console.log(candidateValue);
    return candidateValue;
  }

  function selectCandidate(candidates) {
    let result1 = [];
    let maxV = -Infinity;
    for (const obj of candidates) {
      if (obj.v > maxV) {
        maxV = obj.v;
        result1 = [obj];
      } else if (obj.v === maxV) {
        result1.push(obj);
      }
    }

    if (result1.length === 1) {
      return result1[0];
    }

    let result2 = [];
    let minA = Infinity;
    for (const obj of result1) {
      if (obj.a < minA) {
        minA = obj.a;
        result2 = [obj];
      } else if (obj.a === minA) {
        result2.push(obj);
      }
    }

    if (result2.length === 1) {
      return result2[0];
    }

    let result3 = [];
    let minX = Infinity;
    for (const obj of result2) {
      if (obj.x < minX) {
        minX = obj.x;
        result3 = [obj];
      } else if (obj.x === minX) {
        result3.push(obj);
      }
    }

    if (result3.length === 1) {
      return result3[0];
    }

    let result4 = [];
    let minY = Infinity;
    for (const obj of result3) {
      if (obj.y < minY) {
        minY = obj.y;
        result4 = [obj];
      } else if (obj.y === minY) {
        result4.push(obj);
      }
    }

    return result4[0];
  }

  function changeBoard({ y, x, a }) {
    const yStart = y - 1;
    const xStart = x - 1;
    const grid = Array.from({ length: 3 }, () => Array(3).fill(0));

    for (let i = yStart; i < yStart + 3; i++) {
      for (let j = xStart; j < xStart + 3; j++) {
        grid[i - yStart][j - xStart] = board[i][j];
      }
    }

    switch (a) {
      // 90도 회전
      case 0:
        for (let i = 0; i < 3; i++) {
          for (let j = 0; j < 3; j++) {
            board[j + yStart][2 - i + xStart] = grid[i][j];
          }
        }
        break;
      // 180도 회전
      case 1:
        for (let i = 0; i < 3; i++) {
          for (let j = 0; j < 3; j++) {
            board[2 - i + yStart][2 - j + xStart] = grid[i][j];
          }
        }
        break;
      // 270도 회전
      case 2:
        for (let i = 0; i < 3; i++) {
          for (let j = 0; j < 3; j++) {
            board[2 - j + yStart][i + xStart] = grid[i][j];
          }
        }
        break;
    }
  }

  function find() {
    const visited = Array.from({ length: 5 }, () => Array(5).fill(false));
    let completedPieces = new Queue([]);
    let value = 0;

    for (let i = 0; i < 5; i++) {
      for (let j = 0; j < 5; j++) {
        if (visited[i][j]) {
          continue;
        }

        let pieces = [];
        const q = new Queue([]);
        q.push([i, j]);
        visited[i][j] = true;
        let cnt = 0;

        while (q.size() > 0) {
          const [curY, curX] = q.pop();
          cnt += 1;
          pieces.push([curY, curX]);
          const curPiece = board[curY][curX];

          for (let d = 0; d < 4; d++) {
            const [newY, newX] = [curY + yDirs[d], curX + xDirs[d]];

            if (newY < 0 || newY >= 5 || newX < 0 || newX >= 5) {
              continue;
            }

            if (visited[newY][newX]) {
              continue;
            }

            if (board[newY][newX] === curPiece) {
              q.push([newY, newX]);
              visited[newY][newX] = true;
            }
          }
        }

        if (cnt >= 3) {
          value += cnt;
          for (const piece of pieces) {
            completedPieces.push(piece);
          }
        }
      }
    }
    // 디버깅
    // debug(board, "bef");

    const isDeleted = Array.from({ length: 5 }, () => Array(5).fill(false));
    for (const piece of completedPieces.toArray()) {
      const [y, x] = piece;
      isDeleted[y][x] = true;
    }

    for (let i = 0; i < 5; i++) {
      for (let j = 4; j >= 0; j--) {
        if (isDeleted[j][i]) {
          board[j][i] = wall.pop();
        }
      }
    }

    // 디버깅
    // debug(board, "after");
    // console.log(value);
    return value;
  }

  for (let k = 0; k < K; k++) {
    let turnValue = 0;
    let candidates = [];

    for (let i = 1; i <= 3; i++) {
      for (let j = 1; j <= 3; j++) {
        for (let a = 0; a < 3; a++) {
          const candidateBoard = getCandidateBoard(i, j, a);
          const candidateValue = getCandidateValue(candidateBoard);
          candidates.push({ y: i, x: j, a: a, v: candidateValue });
        }
      }
    }

    let selected = selectCandidate(candidates);

    if (selected.v === 0) {
      break;
    }

    changeBoard(selected);

    while (true) {
      const value = find();
      if (value === 0) {
        break;
      }

      turnValue += value;
    }

    totalValues.push(turnValue);
  }

  console.log(totalValues.join(" "));
  process.exit();
});

function debug(board, message) {
  console.log(message);
  for (let i = 0; i < 5; i++) {
    console.log(board[i].join(" "));
  }
}
