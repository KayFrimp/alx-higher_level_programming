#!/usr/bin/node

const { argv } = process;

const args = process.argv.length;
if (args <= 2) {
  console.log('No argument');
} else {
  console.log(`${argv[2]}`);
}
