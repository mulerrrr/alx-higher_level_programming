#!/usr/bin/node
if (!process.argv[2] || !Number(process.argv[2])) {
  console.log('Missing size');
} else {
  const size = Number(process.argv[2]);
  for (let index = 0; index < size; index++) {
    console.log('X'.repeat(size));
  }
}
