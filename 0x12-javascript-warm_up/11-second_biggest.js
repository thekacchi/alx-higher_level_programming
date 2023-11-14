#!/usr/bin/node

function findSecondLargest (numbers) {
  const sortedNumbers = numbers.sort((a, b) => b - a);

  if (sortedNumbers.length < 2) {
    return 0;
  }

  return sortedNumbers[1];
}

const args = process.argv.slice(2);
const integerArgs = args.map(arg => parseInt(arg, 10));

console.log(findSecondLargest(integerArgs));
