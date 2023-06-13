#!/usr/bin/node
// Reverse a given list
exports.esrever = function (list) {
  const reverseList = [];
  for (let index = 1; index <= list.length; index++) {
    reverseList.push(list[list.length - index]);
  }
  return reverseList;
}
