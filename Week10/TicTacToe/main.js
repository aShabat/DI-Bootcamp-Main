let player = "";
let computer = "";

const board = document.getElementById("board");
let boardData = Array(9).fill("");
const startMenu = document.getElementById("start");
const endMenu = document.getElementById("result");

for (const choice of ["X", "O"]) {
  document.getElementById("start" + choice).addEventListener("click", (_) => {
    player = choice;
    computer = player == "X" ? "O" : "X";
    board.style.setProperty("display", "table");
    startMenu.style.setProperty("display", "none");
  });
}

for (const cell of board.getElementsByTagName("td")) {
  cell.addEventListener("click", (_) => playerTurn(cell));
}

function playerTurn(cell) {
  const id = Number(cell.id);
  boardData[id] = player;
  if (cell.innerHTML !== "") return;

  cell.innerHTML = player;
  if (!checkWinner()) {
    // computerTurn(computerRandomTurn());
    computerTurn(computerSmartTurn());
  }
}

function computerTurn(id) {
  boardData[id] = computer;
  document.getElementById(id).innerHTML = computer;
  checkWinner();
}

const winningLines = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6],
];

function randomArrayElement(array) {
  return array[Math.floor(Math.random() * array.length)];
}

function computerRandomTurn() {
  return randomArrayElement(
    Array.from(Array(9).keys()).filter((i) => boardData[i] === ""),
  );
}

function computerSmartTurn() {
  const [winningTurn, blockingTurn, randomTurn] = [[], [], []];
  winningLines.forEach((line) => {
    const emptyCells = line.filter((i) => boardData[i] === "");
    const playerCells = line.filter((i) => boardData[i] === player);
    const computerCells = line.filter((i) => boardData[i] === computer);

    if (emptyCells.length === 1 && computerCells.length === 2)
      winningTurn.push(...emptyCells);
    if (emptyCells.length === 1 && playerCells.length === 2)
      blockingTurn.push(...emptyCells);
    if (emptyCells.length === 2 && computerCells.length === 1)
      randomTurn.push(...emptyCells);
  });

  if (winningTurn.length > 0) return randomArrayElement(winningTurn);
  if (blockingTurn.length > 0) return randomArrayElement(blockingTurn);
  if (randomTurn.length > 0) return randomArrayElement(randomTurn);
  return computerRandomTurn();
}

function checkWinner() {
  let winner = "";
  for (const line of winningLines) {
    const lineCells = boardData.filter((_, i) => line.includes(i));
    if (lineCells.every((c) => c === player)) {
      winner = "You";
      break;
    }
    if (lineCells.every((c) => c === computer)) {
      winner = "Computer";
      break;
    }
  }

  if (winner === "" && boardData.every((c) => c !== "")) winner = "Nobody";
  if (winner !== "") {
    result.style.setProperty("display", "block");

    document.getElementById("winner").innerHTML = winner;
    return true;
  }
  return false;
}

document.getElementById("restart").addEventListener("click", (_) => {
  board.style.setProperty("display", "none");
  result.style.setProperty("display", "none");
  startMenu.style.setProperty("display", "block");
  player = "";
  computer = "";
  boardData.fill("");
  for (const cell of board.getElementsByTagName("td")) {
    console.log(cell);
    cell.innerHTML = "";
  }
});
