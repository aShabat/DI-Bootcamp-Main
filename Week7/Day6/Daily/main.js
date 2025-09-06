// In this exercise we will be creating a webpage with a black background as the solar system and we will fill the solar system with planets and their moons.
// We will provide the HTML page.
// You only have to work with a JS file.
//
//     Create an array which value is the planets of the solar system.
//     For each planet in the array, create a <div> using createElement. This div should have a class named "planet".
//     Each planet should have a different background color. (Hint: you could add a new class to each planet - each class containing a different background-color).
//     Finally append each div to the <section> in the HTML (presented below).
//     Bonus: Do the same process to create the moons.
//         Be careful, each planet has a certain amount of moons. How should you display them?
//         Should you still use an array for the planets ? Or an array of objects ?

const planets = [
  ["Mercury", "white"],
  ["Venus", "yellow"],
  ["Earth", "green"],
  ["Mars", "red"],
  ["Jupyter", "orange"],
  ["Saturn", "darkyellow"],
  ["Uranus", "lightblue"],
  ["Neptune", "darkblue"],
];

const section = document.getElementsByTagName("section")[0];
for (planet_color of planets) {
  const planet = planet_color[0];
  const color = planet_color[1];
  const div = document.createElement("div");
  div.className = "planet";
  div.style.backgroundColor = color;
  div.innerHTML = planet;
  section.appendChild(div);
}
