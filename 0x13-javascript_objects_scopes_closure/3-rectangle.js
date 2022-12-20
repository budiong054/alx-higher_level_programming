#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let charX = '';
      for (let j = 0; j < this.width; j++) {
        charX += 'X';
      }
      console.log(charX);
    }
  }
};