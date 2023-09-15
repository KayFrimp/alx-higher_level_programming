#!/usr/bin/node

function factorial (x) {
  if (!x) {
    return 1;
  }
  if (x <= 0) {
    return 1;
  }
  return x * factorial(x - 1);
}

const { argv } = process;

console.log(factorial(parseInt(argv[2])));
