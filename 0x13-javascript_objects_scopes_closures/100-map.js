#!/usr/bin/node
// Script that imports an array and computes a new array.
const listImport = require('./100-data.js').list;
let index = -1;
const newList = listImport.map(x => {
  index += 1;
  return x * index;
});
console.log(listImport);
console.log(newList);

