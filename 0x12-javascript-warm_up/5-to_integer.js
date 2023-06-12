#!/usr/bin/node
if (!process.argv[2] || !Number(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(process.argv[2]));
}
