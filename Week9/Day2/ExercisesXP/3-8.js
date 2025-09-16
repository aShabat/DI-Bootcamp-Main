// 🌟 Exercise 3 : Is it a string ?
// Instructions
//
//     Write a JavaScript arrow function that checks whether the value of the argument passed, is a string or not. The function should return true or false
//     Check out the example below to see the expected output
//
// Example:
//
// console.log(isString('hello'));
// //true
// console.log(isString([1, 2, 4, 0]));
// //false

const isString = (variable) => typeof variable === "string";

console.log(isString("hello"));
console.log(isString([1, 2, 4, 0]));

// 🌟 Exercise 4 : Find the sum
// Instructions
//
//     Create a one line function (ie. an arrow function) that receives two numbers as parameters and returns the sum.

const sum = (a, b) => a + b;

// 🌟 Exercise 5 : Kg and grams
// Instructions
//
// Create a function that receives a weight in kilograms and returns it in grams. (Hint: 1 kg is 1000gr)
//
//     First, use function declaration and invoke it.
//     Then, use function expression and invoke it.
//     Write in a one line comment, the difference between function declaration and function expression.
//     Finally, use a one line arrow function and invoke it.

function convertDecl(mass) {
  return mass * 1000;
}
console.log(convertDecl(5));

const convertExpr = function (mass) {
  return mass * 1000;
};
console.log(convertExpr(5));

// convertDecl is hoisted and can be used earlier in the programm, but convertExpr isn't

const convertArrow = (mass) => mass * 1000;
console.log(convertArrow(5));

// 🌟 Exercise 6 : Fortune teller
// Instructions
//
//     Create a self invoking function that takes 4 arguments: number of children, partner’s name, geographic location, job title.
//     The function should display in the DOM a sentence like "You will be a <job title> in <geographic location>, and married to <partner's name> with <number of children> kids."

(function (childrens, name, location, job) {
  const div = document.createElement("div");
  div.innerHTML = `You will be a ${job} in ${location}, and married to ${name} with ${childrens} kids.`;

  document.appendChild(div);
})(5, "Lara", "LA", "billioner");

// 🌟 Exercise 7 : Welcome
// Instructions
//
// John has just signed in to your website and you want to welcome him.
//
//     Create a Navbar in your HTML file.
//     In your js file, create a self invoking funtion that takes 1 argument: the name of the user that just signed in.
//     The function should add a div in the nabvar, displaying the name of the user and his profile picture.

(function (name) {
  const div = document.createElement("div");
  div.innerHTML = `${name} <img src='./profiles/${name}.png`;

  const nav = document.getElementById("nav");
  nav.appendChild(div);
});

// 🌟 Exercise 8 : Juice Bar
// Instructions
//
// You will use nested functions, to open a new juice bar.
// Part I:
//
//     The outer function named makeJuice receives 1 argument: the size of the beverage the client wants - small, medium or large.
//
//     The inner function named addIngredients receives 3 ingredients, and displays on the DOM a sentence like The client wants a <size drink> juice, containing <first ingredient>, <second ingredient>, <third ingredient>".
//
//     Invoke the inner function ONCE inside the outer function. Then invoke the outer function in the global scope.
//
//
// Part II:
//
//     In the makeJuice function, create an empty array named ingredients.
//
//     The addIngredients function should now receive 3 ingredients, and push them into the ingredients array.
//
//     Create a new inner function named displayJuice that displays on the DOM a sentence like The client wants a <size drink> juice, containing <first ingredient>, <second ingredient>, <third ingredient>".
//
//     The client wants 6 ingredients in his juice, therefore, invoke the addIngredients function TWICE. Then invoke once the displayJuice function. Finally, invoke the makeJuice function in the global scope.

function makeJuice(size) {
  const ingredients = [];
  function addIngredients(first, second, third) {
    ingredients.push(first);
    ingredients.push(second);
    ingredients.push(third);
  }

  function displayJuice() {
    const div = document.createElement("div");
    div.innerHTML = `The client wants a ${size} juice, containing`;
    for (const ingredient of ingredients) {
      div.innerHTML += " " + ingredient;
    }
    div.innerHTML += ".";

    document.appendChild(div);
  }

  addIngredients("apple", "cherry", "banana");
  addIngredients("tomato", "mango", "pineapple");

  displayJuice();
}

makeJuice("small");
