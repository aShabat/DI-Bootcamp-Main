// 🌟 Exercise 1 : List of people
// Instructions
//
// const people = ["Greg", "Mary", "Devon", "James"];
//
//
// Part I - Review about arrays
//
//     Write code to remove “Greg” from the people array.
//
//     Write code to replace “James” to “Jason”.
//
//     Write code to add your name to the end of the people array.
//
//     Write code that console.logs Mary’s index. take a look at the indexOf method on Google.
//
//     Write code to make a copy of the people array using the slice method.
//         The copy should NOT include “Mary” or your name.
//         Hint: remember that now the people array should look like this const people = ["Mary", "Devon", "Jason", "Yourname"];
//         Hint: Check out the documentation for the slice method
//
//     Write code that gives the index of “Foo”. Why does it return -1 ?
//
//     Create a variable called last which value is the last element of the array.
//     Hint: What is the relationship between the index of the last element in the array and the length of the array?
//
//
// Part II - Loops
//
//     Using a loop, iterate through the people array and console.log each person.
//
//     Using a loop, iterate through the people array and exit the loop after you console.log “Devon” .
//     Hint: take a look at the break statement in the lesson.
const people = ["Greg", "Mary", "Devon", "James"];

var my_people = people.slice(1);
my_people[2] = "Jason";
my_people.push("Anton");
console.log(my_people.indexOf("Mary"));
var another_people = my_people.slice(0, 1).concat(my_people.slice(2, -1));
console.log(my_people.indexOf("Foo"));
var last = my_people[my_people.length - 1];

for (person of my_people) {
  console.log(person);
}

for (person of my_people) {
  console.log(person);
  if (person == "Devon") break;
}

// 🌟 Exercise 2 : Your favorite colors
// Instructions
//
//     Create an array called colors where the value is a list of your five favorite colors.
//     Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
//     Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
//     Hint : create an array of suffixes to do the Bonus

var colors = ["red", "green", "blue", "yellow", "orange"];
for (c in colors) {
  c++;
  switch (c) {
    case 1:
      console.log("My 1st choise is " + colors[c]);
      break;
    case 2:
      console.log("My 2nd choice is " + colors[c]);
      break;
    case 3:
      console.log("My 3rd choice is " + colors[c]);
      break;
    default:
      console.log("My " + c + "th choice is " + colors[c]);
  }
}

// 🌟 Exercise 3 : Repeat the question
// Instructions
//
//     Prompt the user for a number.
//     Hint : Check the data type you receive from the prompt (ie. Use the typeof method)
//
//     While the number is smaller than 10 continue asking the user for a new number.
//     Tip : Which while loop is more relevant for this situation?

var num;
do {
  num = Number(prompt("write a number"));
} while (isNaN(num) || num < 10);

// 🌟 Exercise 4 : Building Management
// Instructions:
//
// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },
//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan:  [4, 1000],
//         david: [1, 500],
//     },
// }
//
//
// Review about objects
//
//     Copy and paste the above object to your Javascript file.
//
//     Console.log the number of floors in the building.
//
//     Console.log how many apartments are on the floors 1 and 3.
//
//     Console.log the name of the second tenant and the number of rooms he has in his apartment.
//
//     Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.

const building = {
  numberOfFloors: 4,
  numberOfAptByFloor: {
    firstFloor: 3,
    secondFloor: 4,
    thirdFloor: 9,
    fourthFloor: 2,
  },
  nameOfTenants: ["Sarah", "Dan", "David"],
  numberOfRoomsAndRent: {
    sarah: [3, 990],
    dan: [4, 1000],
    david: [1, 500],
  },
};

console.log(building.numberOfFloors);
console.log(
  building.numberOfAptByFloor.firstFloor,
  building.numberOfAptByFloor.thirdFloor,
);

console.log(
  building.nameOfTenants[1],
  building.numberOfRoomsAndRent.dan.length,
);

if (
  building.numberOfRoomsAndRent.sarah[1] +
    building.numberOfRoomsAndRent.david[1] >
  building.numberOfRoomsAndRent.dan[1]
) {
  building.numberOfRoomsAndRent.dan = 1200;
}

// Exercise 6 : Rudolf
// Instructions
//
// const details = {
//   my: 'name',
//   is: 'Rudolf',
//   the: 'reindeer'
// }
//
//     Given the object above and using a for loop, console.log “my name is Rudolf the reindeer”

const details = {
  my: "name",
  is: "Rudolf",
  the: "reindeer",
};

var result = "";
for (key in details) {
  result += key + " " + details[key] + " ";
}
console.log(result);

// Exercise 7 : Secret Group
// Instructions
//
// const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
//
//     A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
//     Hint: a string is an array of letters
//     Console.log the name of their secret society. The output should be “ABJKPS”

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
var secres_society_name = [];
for (n of names) {
  secres_society_name.push(n[0]);
}
console.log(secres_society_name.sort().join(""));
