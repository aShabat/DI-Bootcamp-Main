const infoDiv = document.getElementById("info");
const findButton = document.getElementById("find");

const personUrl = "https://swapi.tech/api/people/";
const maxId = 83;

findButton.addEventListener("click", async () => {
  loading();
  try {
    const response = await fetch(
      personUrl + (Math.floor(Math.random() * maxId) + 1),
    );
    if (!response.ok) throw "This person isn't awailable";
    else {
      const result = await response.json();
      const planet = await fetchPlanet(result.result.properties.homeworld);
      info(result.result.properties, planet);
    }
  } catch (e) {
    error(e);
  }
});

function loading() {
  infoDiv.innerHTML = "Loading...";
}

function error(e) {
  infoDiv.innerHTML = `Oh no! ${e}!`;
}

async function info(props, planet) {
  infoDiv.innerHTML = `
  <h2>${props.name}</h2>
  <p>Height: ${props.height}</p>
  <p>Gender: ${props.gender}</p>
  <p>Birth Year: ${props.birth_year}</p>
  <p>Home World: ${planet}</p>
  `;
}

async function fetchPlanet(url) {
  const response = await fetch(url);
  if (!response.ok) throw "The planet isn't available";
  const result = await response.json();
  return result.result.properties.name;
}
