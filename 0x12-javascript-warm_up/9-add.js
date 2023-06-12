#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

const first = Number(process.argv[2]);
const second = Number(process.argv[3]);
add(first, second);
