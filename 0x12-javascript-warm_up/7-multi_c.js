#!/usr/bin/node

const { argv } = process;

let convertedInt = parseInt(argv[2]);
if (convertedInt) {
  while (convertedInt > 0) {
    console.log('C is fun');
    convertedInt--;
  }
} else {
  console.log('Missing number of occurrences');
}
