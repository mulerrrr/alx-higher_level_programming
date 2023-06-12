#!/usr/bin/node
const myVar = 'C is fun';
const times = process.argv[2];
let iteration = 0;
for (iteration; iteration < times; iteration++) {
  console.log(myVar);
}
