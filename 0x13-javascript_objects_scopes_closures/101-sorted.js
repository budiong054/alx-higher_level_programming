#!/usr/bin/node
const dict = require('./101-data').dict;

// Get all the value in an  array
const newArray = [];
for (const key in dict) {
  newArray.push(dict[key]);
}

// Create a new dictionary with the unique value in the newArray
const newDict = {};
for (const element of [...new Set(newArray)]) {
  newDict[element] = [];
}

// Push the keys to the new dictionary with corresponding value
for (const key in dict) {
  newDict[dict[key]].push(key);
}
console.log(newDict);
