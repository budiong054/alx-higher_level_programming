#!/usr/bin/node
// This script prints two arguments passed to it, in the following format:
// "is"

const argv = process.argv;

console.log(`${argv[2]} is ${argv[3]}`);
