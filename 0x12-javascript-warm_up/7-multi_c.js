#!/usr/bin/node
// This script prints "x" times "C is fun"

const firstArg = process.argv[2];

if (isNaN(firstArg)) {
  console.log('Missing number of occurrences');
} else {
  const num = parseInt(firstArg);
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
