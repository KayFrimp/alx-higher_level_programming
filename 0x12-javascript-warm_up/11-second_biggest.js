#!/usr/bin/node

const { argv } = process;
const args = process.argv.length;

if (args <= 2) {
  console.log(0);
} else if (args === 3) {
  console.log(0);
} else {
  let firstLargest = argv[0];
  let secondLargest = argv[0];

  for (let i = 0; i < argv.length; i++) {
    if (argv[i] > firstLargest) {
      secondLargest = firstLargest;
      firstLargest = argv[i];
    } else if (argv[i] > secondLargest && argv[i] !== firstLargest) {
      secondLargest = argv[i];
    }
  }

  console.log(secondLargest);
}
