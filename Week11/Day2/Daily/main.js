const form = document.getElementById("main");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const data = new FormData(form);
  const dataJSON = JSON.stringify(Object.fromEntries(data));

  const newDiv = document.createElement("div");
  newDiv.innerHTML = dataJSON;
  form.parentNode.appendChild(newDiv);
});
