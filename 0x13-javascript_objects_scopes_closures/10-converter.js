#!/usr/bin/node

exports.converter = (base) => {
  return function (num) {
	  return num.toString(base);
  }
}
