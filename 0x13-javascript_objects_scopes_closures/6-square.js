#!/usr/bin/node
const Square = require('./5-square');

module.exports = class extends Square {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      let charX = '';
      for (let j = 0; j < this.size; j++) {
        charX += c;
      }
      console.log(charX);
    }
  }
};
