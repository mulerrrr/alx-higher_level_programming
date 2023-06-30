#!/usr/bin/node
// Script that imports a dictionary of occurrences by user id
// and computes a dictionary of user ids by occurrence.
const dictImport = require('./101-data.js').dict;
const newDict = {};
for (const key in dictImport) {
  if (newDict[dictImport[key]] === undefined) {
    newDict[dictImport[key]] = [key];
  } else {
    newDict[dictImport[key]].push(key);
  }
}
console.log(newDict);
