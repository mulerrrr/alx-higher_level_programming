#!/usr/bin/node
// gets the contents of a webpage and stores it in a file.
const request = require('request');
const url = process.argv[2];
const bodyFile = process.argv[3];
const fs = require('fs');
request(url, 'utf-8', (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(bodyFile, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
