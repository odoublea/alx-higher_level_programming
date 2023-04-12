#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      const printC = c.repeat(this.width);
      for (let i = 0; i < this.height; i++) {
        console.log(printC);
      }
    }
  }
}

module.exports = Square;
