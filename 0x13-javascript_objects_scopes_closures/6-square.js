#!/usr/bin/node
// Class Square that inherits from Rectangle class

module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let hei = 0; hei < this.height; hei++) {
      let result = '';
      for (let wid = 0; wid < this.width; wid++) {
        result += c;
      }
      console.log(result);
    }
  }
};
