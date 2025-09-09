const button = document.getElementById("jsstyle");
button.style.backgroundColor = "white";
button.style.fontSize = "10rem";

button.addEventListener("mouseover", () => {
  button.style.backgroundColor = "red";
  button.style.fontWeight = "bold";
});

button.addEventListener("mouseleave", () => {
  button.style.backgroundColor = "white";
  button.style.fontWeight = "normal";
});

button.addEventListener("click", () => {
  alert("Don't click the big red button!!!");
});
