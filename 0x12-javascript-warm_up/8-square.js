#!/usr/bin/node
// This script prints a square

const size = process.argv[2];
let charX;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(size); i++) {
    charX = '';
    for (let j = 0; j < parseInt(size); j++) {
      charX += 'X';
    }
    console.log(charX);
  }
}
