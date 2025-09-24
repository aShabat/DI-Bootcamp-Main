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
  if (!checkWinner()) computerTurn();
}

function computerTurn() {
  for (let i = 0; i < 1000; i++) {
    const id = Math.floor(Math.random() * 9);
    if (boardData[id] !== "") continue;
    boardData[id] = computer;
    document.getElementById(id).innerHTML = computer;
    checkWinner();
    return;
  }
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

function checkWinner() {
  let winner = "";
  if (boardData.every((c) => c !== "")) winner = "Nobody";
  else
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
