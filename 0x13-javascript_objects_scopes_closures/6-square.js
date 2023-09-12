#!/usr/bin/node

const parentSquare = require('./5-square');

class Square extends parentSquare {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }

    for (let x = 0; x < this.height; x++) {
      let rect = '';
      for (let y = 0; y < this.width; y++) {
        rect = rect + c;
      }
      console.log(rect);
    }
  }
}

module.exports = Square;
