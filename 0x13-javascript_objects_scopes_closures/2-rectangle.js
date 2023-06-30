#!/usr/bin/node
// Class Rectangle that defines a rectangle with width and height
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w !== 0 && h !== 0) && (w > 0 && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
}; // used to export just one thing
