#!/usr/bin/node
// Count number of ocurrences in a given list
exports.nbOccurences = function (list, searchElement) {
  let ocurrences = 0;
  for (let index = 0; index < list.length; index++) {
    if (list[index] === searchElement) {
      ocurrences += 1;
    }
  }
  return ocurrences;
};
