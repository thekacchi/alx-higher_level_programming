#!/usr/bin/node

const arg = process.argv[2];
const parg = parseInt(arg, 10);

if (!isNaN(parg)) {
  console.log('My Number: ' + parg);
} else {
  console.log('Not a number');
}
