#!/usr/bin/node

const fs = require('fs');

// Receiving the file from the command line
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

// Reading the content of the file
const dataA = fs.readFileSync(fileA, 'utf8');
const dataB = fs.readFileSync(fileB, 'utf8');

// Concatinating the data
const dataC = dataA + dataB;

// writing the new data into the destination file
fs.writeFileSync(fileC, dataC);
