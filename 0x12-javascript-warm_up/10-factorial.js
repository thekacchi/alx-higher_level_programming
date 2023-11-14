#!/usr/bin/node

function computeFactorial (n) {
  if (isNaN(n)) {
    return 1;
  }

  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * computeFactorial(n - 1);
  }
}

const args = process.argv.slice(2);
const inputNumber = parseInt(args[0], 10);

if (!isNaN(inputNumber)) {
  const result = computeFactorial(inputNumber);
  console.log(result);
} else {
  console.log('1');
}
