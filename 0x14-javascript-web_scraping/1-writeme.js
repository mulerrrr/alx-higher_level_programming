#!/usr/bin/node
// write a string to a file
const fs = require('fs');
const data = process.argv[3];
const fileName = process.argv[2];
fs.writeFile(fileName, data, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
