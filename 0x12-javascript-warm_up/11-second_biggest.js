#!/usr/bin/node
// This script searches the second biggest integer in the list of arguments

const [, , ...args] = process.argv;

const array = [...new Set(args.map(el => parseInt(el)))];

if (array.length <= 1) {
  console.log(0);
} else {
  array.sort();
  console.log(array[array.length - 2]);
}
