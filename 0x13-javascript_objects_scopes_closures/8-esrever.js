#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  const listLength = list.length - 1;

  for (let i = listLength; i > -1; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
