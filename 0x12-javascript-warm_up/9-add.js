#!/usr/bin/node

function add(a, b) {
  return (a + b);
}

const arga = process.argv[2];
const argb = process.argv[3];

const pa = parseInt(arga, 10);
const pb = parseInt(argb, 10);

if (!isNaN(pa) && !isNaN(pb)) {
  sum = add(pa, pb);
  console.log(sum);
} else {
  sum = add(pa, pb);
  console.log(sum);
}
