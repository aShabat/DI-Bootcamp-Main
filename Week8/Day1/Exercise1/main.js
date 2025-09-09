let row_num = 3;
function insertRow() {
  const table = document.getElementById("sampleTable");
  const row = document.createElement("tr");

  // const cell1 = document.createElement("td");
  // const cell2 = document.createElement("td");
  // cell1.innerHTML = "Row" + row_num + " cell1";
  // cell2.innerHTML = "Row" + row_num + " cell2";
  // row.appendChild(cell1);
  // row.appendChild(cell2);

  row.innerHTML =
    "<td>Row" + row_num + " cell1</td><td>Row" + row_num + " cell2</td>";

  table.appendChild(row);
  row_num++;
}
