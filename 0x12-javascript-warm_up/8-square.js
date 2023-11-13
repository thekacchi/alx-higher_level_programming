#!/usr/bin/node

const sizearg = process.argv[2];
const size = parseInt(sizearg, 10);

if (isNaN(size)) {
  console.log('Missing Size');
} else {
  let counter = 0;
  while (counter < size) {
    console.log('X'.repeat(size));
    counter++;
  }
}
