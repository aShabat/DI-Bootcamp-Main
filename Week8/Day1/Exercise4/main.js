const form = document.getElementById("form1");
form.addEventListener("submit", getvalue);

function getvalue(e) {
  e.preventDefault();
  const elements = e.target.elements;
  alert(elements["fname"].value);
  alert(elements["lname"].value);
}
