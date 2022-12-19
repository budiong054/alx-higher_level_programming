#!/usr/bin/node
// This script searches the second biggest integer in the list of arguments

const argv = process.argv;
let secondMax;
let max;

if (argv.length <= 3) {
  console.log(0);
} else {
  max = secondMax = parseInt(argv[2]);
  for (let i = 3; i < argv.length; i++) {
    if (max <= parseInt(argv[i])) {
      secondMax = max;
      max = parseInt(argv[i]);
    }
  }
  console.log(secondMax);
}
