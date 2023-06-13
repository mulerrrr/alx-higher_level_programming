#!/usr/bin/node
// Class Rectangle that defines a rectangle with width and height
// Add print instance method
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w !== 0 && h !== 0) && (w > 0 && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let hei = 0; hei < this.height; hei++) {
      let result = '';
      for (let wid = 0; wid < this.width; wid++) {
        result += 'X';
      }
      console.log(result);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}; // used to export just one thing
