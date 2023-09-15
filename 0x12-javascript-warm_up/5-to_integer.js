#!/usr/bin/node

const { argv } = process;

const convertedInt = parseInt(argv[2]);
if (convertedInt) {
  console.log(`My number: ${convertedInt}`);
} else {
  console.log('Not a number');
}
