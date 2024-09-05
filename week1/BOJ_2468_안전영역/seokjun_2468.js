// 영역 생성
// 비의 양이 1-높이의 최대값인 경우에 따라서 안전영역 최대 개수 구하기
// dfs로 탐색하여 안전영역 구하기
// 구한 안전영역이 최대값보다 크면 업데이트
// 결과값 리턴

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
let currentLine = 0;

rl.on("line", (line) => {
  input.push(line.split(" ").map(Number));
});

rl.on("close", () => {
  const N = input[currentLine++];
  const field = Array.from({ length: N }, () => []);
  let maxHeight = -Infinity;

  for (let n = 0; n < N; n++) {
    for (let i = 0; i < input[currentLine].length; i++) {
      let height = input[currentLine][i];
      field[i].push(height);
      if (height > maxHeight) {
        maxHeight = height;
      }
    }
    currentLine += 1;
  }

  const rainField = (rain) => {
    const newField = Array.from({ length: N }, () =>
      Array.from({ length: N }, () => 1)
    );

    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        if (field[i][j] <= rain) {
          newField[i][j] = 0;
        }
      }
    }

    return newField;
  };

  const dirs = [1, -1, 0, 0, 1, -1];
  const dfs = (board, x, y) => {
    board[x][y] = 0;

    for (let i = 0; i < 4; i++) {
      const newX = x + dirs[i];
      const newY = y + dirs[i + 2];

      if (
        newX < 0 ||
        newY < 0 ||
        newX >= N ||
        newY >= N ||
        board[newX][newY] === 0
      ) {
        continue;
      }

      dfs(board, newX, newY);
    }
  };

  let maxSafeArea = -Infinity;

  for (let rain = 0; rain < maxHeight; rain++) {
    const fieldAfterRain = rainField(rain);
    let safeArea = 0;

    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        if (fieldAfterRain[i][j] === 1) {
          dfs(fieldAfterRain, i, j);
          safeArea += 1;
        }
      }
    }

    if (safeArea > maxSafeArea) {
      maxSafeArea = safeArea;
    }
  }

  console.log(maxSafeArea);
});
