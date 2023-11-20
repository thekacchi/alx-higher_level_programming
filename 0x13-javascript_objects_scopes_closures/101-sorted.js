#!/usr/bin/node

const { dict } = require('./101-data');


function invertOccurrencesDict(inputDict)
{
  const resultDict = {};

  for (const userId in inputDict) {
    const occurrences = inputDict[userId];

    if (!resultDict[occurrences]) {
      resultDict[occurrences] = [];
    }

    resultDict[occurrences].push(userId.toString());
  }

  return (resultDict);
}

// Compute the new dictionary
const invertedDict = invertOccurrencesDict(dict);

// Print the new dictionary
console.log(invertedDict);
