const colors = [
  "red",
  "orangered",
  "orange",
  "yellow",
  "yellowgreen",
  "lightgreen",
  "green",
  "turquoise",
  "cyan",
  "lightskyblue",
  "dodgerblue",
  "blue",
  "darkblue",
  "indigo",
  "darkmagenta",
  "violet",
  "lightpink",
  "lightgray",
  "gray",
  "black",
  "white",
];

const menu = document.getElementById("color_menu");
let selected_color = null;
function select_color(event) {
  selected_color = event.target.style.backgroundColor;
}
for (const color of colors) {
  const color_button = document.createElement("div");
  color_button.style.backgroundColor = color;
  color_button.classList.add("color_button");
  color_button.addEventListener("click", select_color);

  menu.appendChild(color_button);
}

const grid = document.getElementById("grid");
const grid_width = 10;
const grid_height = 10;
let grid_cells = null;

const body = document.getElementsByTagName("body")[0];
let mouse_down = false;
body.addEventListener("mousedown", (_) => (mouse_down = true));
body.addEventListener("mouseup", (_) => (mouse_down = false));

function set_grid_dimensions(width, height) {
  grid.style.setProperty("grid-template-rows", "repeat(" + height + ",1fr)");
  grid.style.setProperty("grid-template-columns", "repeat(" + width + ",1fr)");
  grid_cells = Array(height)
    .fill(null)
    .map((_) =>
      Array(width)
        .fill(null)
        .map((_) => document.createElement("div")),
    );

  grid.childNodes = [];
  for (const row of grid_cells) {
    for (const cell of row) {
      cell.classList.add("cell");
      cell.addEventListener("mousedown", (e) => {
        if (selected_color !== null)
          e.target.style.backgroundColor = selected_color;
      });
      cell.addEventListener("mouseover", (e) => {
        if (selected_color !== null && mouse_down)
          e.target.style.backgroundColor = selected_color;
      });
      grid.appendChild(cell);
    }
  }
}

set_grid_dimensions(grid_width, grid_height);

const clear_button = document.getElementById("clear_button");
clear_button.addEventListener("click", (_) => {
  for (const cell of grid.childNodes) {
    cell.style.backgroundColor = "white";
    selected_color = null;
  }
});
