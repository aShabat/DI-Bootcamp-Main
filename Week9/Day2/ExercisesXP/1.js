// Instructions
//
//     Analyse the code below, and predict what will be the value of a in all the following functions.
//     Write your prediction as comments in a js file. Explain your predictions.

// #1
function funcOne() {
  let a = 5;
  if (a > 1) {
    a = 3;
  }
  alert(`inside the funcOne function ${a}`);
}

// #1.1 - run in the console:
//
// The programm will alert that a = 3
funcOne();
// #1.2 What will happen if the variable is declared
// with const instead of let ?
//
// The programm will get an error

//#2
let a = 0;
function funcTwo() {
  a = 5;
}

function funcThree() {
  alert(`inside the funcThree function ${a}`);
}

// #2.1 - run in the console:
//
// the programm will first alert that a = 0, then that a = 5
funcThree();
funcTwo();
funcThree();
// #2.2 What will happen if the variable is declared
// with const instead of let ?
//
// programm will alert that a = 0, then will get an error during funcTwo

//#3
function funcFour() {
  window.a = "hello";
}

function funcFive() {
  alert(`inside the funcFive function ${a}`);
}

// #3.1 - run in the console:
//
// if we count declaration of a from previous part the programm will alert that a = 5. otherwise it's undefined. funcFour doesn't affect a
funcFour();
funcFive();

//#4
let a = 1;
function funcSix() {
  let a = "test";
  alert(`inside the funcSix function ${a}`);
}

// #4.1 - run in the console:
//
// alert that a = 'test'
funcSix();
// #4.2 What will happen if the variable is declared
// with const instead of let ?
//
// nothing changes because there are two different a variables

//#5
let a = 2;
if (true) {
  let a = 5;
  alert(`in the if block ${a}`);
}
alert(`outside of the if block ${a}`);

// #5.1 - run the code in the console
//
// alerts that a = 5, then that a = 2
// #5.2 What will happen if the variable is declared
// with const instead of let ?
//
// nothing changes, different variables
