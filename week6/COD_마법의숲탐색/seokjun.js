const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

rl.on("line", (line) => input.push(line));

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
    return this.items[this.front++];
  }
}
/*
마법의 숲: R개의 행, C개의 열. 격자는 1부터 R까지. 북쪽에서 입장 가능.
정령과 골렘: K명. 골렘은 십자 모양으로 5칸 차지. 4개 방향 중 하나는 출구임. 탑승은 4방향 모두 가능, 하차는 출구로만 가능.
탐색 차례 i, 골렘 중앙 c(2~C-1열), 출구 방향 d(0123: 북동남서)

골렘 이동 방법: 더 이상 이동 불가능할 때까지 아래 과정을 반복함.
1. 아래 세 칸 비어 있는 경우 -> 남쪽으로 한 칸 이동
2. 1의 방법 불가능할 시, 왼쪽 세 칸 비어 있는 경우 and 왼쪽 이동 후 아래 세 칸 비어 있는 경우 -> 서&남으로 이동 및 출구 '반시계' 방향으로 이동
3. 2의 방법 불가능할 시, 오른쪽 세 칸 비어 있는 경우 and 오른쪽 이동 후 아래 세 칸 비어 있는 경우 -> 동&남으로 이동 및 출구 '시계' 방향으로 이동

골렘이 더 이상 남쪽으로 이동 불가능 한 경우 정령이 이동함.
정령은 골렘 내에서 상하좌우 인접 칸으로 이동 가능함. 
정령이 속한 골렘의 출구가 다른 골렘과 인접하고 있다면 해당 출구를 통해 다른 골렘으로 이동 가능함.
정령은 갈 수 있는 칸 중 가장 남쪽의 칸으로 이동하고 이동은 완전 종료함.
이동은 종료한 후, 정령의 최종 위치의 행 번호를 반환함.

단, 골렘이 최대한 남쪽으로 이동했는데, 몸이 숲 밖에 삐져나와 있으면, 
현재 골렘과 숲에 남아있는 모든 골렘을 삭제함.
이 경우의 정령 위치는 답에 포함하지 않음.
이후 입장해야할 골렘들이 입장함.
*/

/*
남은 정령과 골렘이 없을 때까지 그들을 입장시킴
    a:
    이동 방법 1이 가능한지 확인
        가능하면 이동 방법 1 실행 후 a로 되돌아 감.
        불가능하면 이동방법 2가 가능한지 확인
            가능하면 이동 방법 2 실행 후 a로 되돌아 감.
            불가능하면 이동 방법 3이 가능한지 확인
                가능하면 이동 방법 3 실행 후 a로 되돌아 감.
                불가능하면 골렘 몸이 숲 밖에 있는지 확인
                    그렇다면 모든 골렘 삭제 후 다음 정령&골렘으로 넘어감. 그렇지 않다면 2번으로
                    그렇지 않다면 정령 이동 실행.
  정령의 최종 위치 행 번호를 답에 추가.
*/

rl.on("close", () => {
  const [R, C, K] = input[0].split(" ").map(Number);
  const golems = [];
  for (let k = 1; k <= K; k++) {
    golems.push(input[k].split(" ").map(Number));
  }

  // 이차원 배열 숲 초기화: 0,1,2번째 행은 숲 밖임.
  const height = R + 3;
  const width = C;
  const forest = Array.from({ length: height }, () =>
    Array.from({ length: width }, () => [0, false])
  );

  // 골렘 중앙 위치로부터 골렘이 중앙, 북, 동, 남, 서 차지하고 있는 위치 반환
  function getCurGolemSpace(curPosition) {
    const [curY, curX] = curPosition;
    return [
      [curY, curX],
      [curY - 1, curX],
      [curY, curX + 1],
      [curY + 1, curX],
      [curY, curX - 1],
    ];
  }

  function isMove1Available(curPosition) {
    const [curCenter, curNorth, curEast, curSouth, curWest] =
      getCurGolemSpace(curPosition);
    if (
      curWest[0] + 1 >= 0 &&
      curWest[0] + 1 < height &&
      forest[curWest[0] + 1][curWest[1]][0] === 0 &&
      curSouth[0] + 1 >= 0 &&
      curSouth[0] + 1 < height &&
      forest[curSouth[0] + 1][curSouth[1]][0] === 0 &&
      curEast[0] + 1 >= 0 &&
      curEast[0] + 1 < height &&
      forest[curEast[0] + 1][curEast[1]][0] === 0
    ) {
      return true;
    }

    return false;
  }

  function move1(curPosition, curExit) {
    curPosition[0] += 1;
  }

  function isMove2Available(curPosition) {
    const [curCenter, curNorth, curEast, curSouth, curWest] =
      getCurGolemSpace(curPosition);
    if (
      curNorth[1] - 1 >= 0 &&
      curNorth[1] - 1 < width &&
      forest[curNorth[0]][curNorth[1] - 1][0] === 0 &&
      curWest[1] - 1 >= 0 &&
      curWest[1] - 1 < width &&
      forest[curWest[0]][curWest[1] - 1][0] === 0 &&
      curSouth[1] - 1 >= 0 &&
      curSouth[1] - 1 < width &&
      forest[curSouth[0]][curSouth[1] - 1][0] === 0 &&
      curWest[0] + 1 >= 0 &&
      curWest[0] + 1 < height &&
      forest[curWest[0] + 1][curWest[1] - 1][0] === 0 &&
      curSouth[0] + 1 >= 0 &&
      curSouth[0] + 1 < height &&
      forest[curSouth[0] + 1][curSouth[1] - 1][0] === 0
    ) {
      return true;
    }

    return false;
  }

  function move2(curPosition, curExit) {
    curPosition[0] += 1;
    curPosition[1] -= 1;
    return curExit !== 0 ? curExit - 1 : 3;
  }

  function isMove3Available(curPosition) {
    const [curCenter, curNorth, curEast, curSouth, curWest] =
      getCurGolemSpace(curPosition);
    if (
      curNorth[1] + 1 >= 0 &&
      curNorth[1] + 1 < width &&
      forest[curNorth[0]][curNorth[1] + 1][0] === 0 &&
      curEast[1] + 1 >= 0 &&
      curEast[1] + 1 < width &&
      forest[curEast[0]][curEast[1] + 1][0] === 0 &&
      curSouth[1] + 1 >= 0 &&
      curSouth[1] + 1 < width &&
      forest[curSouth[0]][curSouth[1] + 1][0] === 0 &&
      curEast[0] + 1 >= 0 &&
      curEast[0] + 1 < height &&
      forest[curEast[0] + 1][curEast[1] + 1][0] === 0 &&
      curSouth[0] + 1 >= 0 &&
      curSouth[0] + 1 < height &&
      forest[curSouth[0] + 1][curSouth[1] + 1][0] === 0
    ) {
      return true;
    }

    return false;
  }

  function move3(curPosition, curExit) {
    curPosition[0] += 1;
    curPosition[1] += 1;
    return curExit !== 3 ? curExit + 1 : 0;
  }

  function isGolemOutside(curPosition) {
    if (curPosition[0] - 1 < 3) {
      return true;
    }

    return false;
  }

  function clearForest() {
    for (let i = 0; i < forest.length; i++) {
      for (let j = 0; j < forest[i].length; j++) {
        forest[i][j] = [0, false];
      }
    }
  }

  function fixGolem(curPosition, curExit, GolemNumber) {
    const golemSpace = getCurGolemSpace(curPosition);
    for (let i = 0; i < golemSpace.length; i++) {
      const [y, x] = golemSpace[i];
      forest[y][x][0] = GolemNumber;

      if (i === curExit + 1) {
        forest[y][x][1] = true;
      }
    }
  }

  const yDirs = [1, 0, -1, 0];
  const xDirs = [0, 1, 0, -1];
  function moveSoulToBottom(soulPosition) {
    const visited = Array.from({ length: height }, () =>
      Array(width).fill(false)
    );
    const q = new Queue();
    q.push(soulPosition);
    visited[soulPosition[0]][soulPosition[1]] = true;

    while (q.size() > 0) {
      const [curY, curX] = q.pop();
      const [curGolemNumber, curIsExit] = forest[curY][curX];

      for (let d = 0; d < 4; d++) {
        let [nextY, nextX] = [curY + yDirs[d], curX + xDirs[d]];

        if (
          nextY < 0 ||
          nextY >= height ||
          nextX < 0 ||
          nextX >= width ||
          visited[nextY][nextX]
        ) {
          continue;
        }

        let [nextGolemNumber, nextIsExit] = forest[nextY][nextX];

        if (nextGolemNumber === 0) {
          continue;
        }

        if (curGolemNumber === nextGolemNumber) {
          q.push([nextY, nextX]);
          visited[nextY][nextX] = true;
        } else if (curIsExit) {
          q.push([nextY, nextX]);
          visited[nextY][nextX] = true;
        }
      }
    }

    // console.log(forest);
    // console.log(visited);

    for (let i = visited.length - 1; i >= 3; i--) {
      if (visited[i].includes(true)) {
        return i - 3 + 1;
      }
    }
  }

  let answer = 0;

  // 골렘이 출발하는 열 c(1-based index, 2 ~ C-1), 골렘의 출구 방향 d(0,1,2,3 -> 북, 동, 남, 서)
  for (let i = 1; i <= K; i++) {
    // 현재 골렘 몸 중앙 위치와 출구 방향
    const [c, d] = golems[i - 1];
    let curPosition = [1, c - 1];
    let soulPosition = curPosition;
    let curExit = d;
    let finalSoulRow = 0;
    // console.log(`${i}번째 골렘: ${c - 1}인덱스 출발, ${d}방향 출구`);

    while (true) {
      if (isMove1Available(curPosition)) {
        move1(curPosition, curExit);
      } else if (isMove2Available(curPosition)) {
        curExit = move2(curPosition, curExit);
      } else if (isMove3Available(curPosition)) {
        curExit = move3(curPosition, curExit);
      } else if (isGolemOutside(curPosition)) {
        clearForest();
        break;
      } else {
        soulPosition = curPosition;
        fixGolem(curPosition, curExit, i);
        finalSoulRow = moveSoulToBottom(soulPosition);
        break;
      }
    }

    answer += finalSoulRow;
  }

  console.log(answer);
  process.exit();
});
