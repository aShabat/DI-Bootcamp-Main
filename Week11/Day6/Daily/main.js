const form = document.getElementById("gifSearch");
const gifsDiv = document.getElementById("gifs");
const deleteAllButton = document.getElementById("deleteAll");
let gifCount = 0;

const apiKey = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My";
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const url = `https://api.giphy.com/v1/gifs/random?api_key=${apiKey}&rating=g&tag=${form.category.value}`;
  // form.category.value = "";

  fetch(url)
    .then((response) => {
      if (response.ok) return response.json();
      else throw `Status: ${response.status}`;
    })
    .then((data) => addGif(data.data.images.original.url))
    .catch((e) => console.log(e));
});

function addGif(url) {
  const newGifDiv = document.createElement("div");

  const newGif = document.createElement("img");
  newGif.setAttribute("src", url);

  const deleteGif = document.createElement("button");
  deleteGif.innerHTML = "Delete";
  deleteGif.addEventListener("click", () => {
    newGifDiv.remove();

    gifCount--;
    if (gifCount === 0) {
      deleteAllButton.style.setProperty("display", "none");
    }
    console.log(deleteAllButton);
  });

  newGifDiv.appendChild(newGif);
  newGifDiv.appendChild(deleteGif);

  gifsDiv.appendChild(newGifDiv);

  if (gifCount === 0) {
    deleteAllButton.style.setProperty("display", "block");
  }
  gifCount++;
}

deleteAllButton.addEventListener("click", () => {
  gifCount = 0;
  gifsDiv.innerHTML = "";
  deleteAllButton.style.setProperty("display", "none");
});
