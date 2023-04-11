#!/usr/bin/node

const num = parseInt(process.argv[2]);
function fact (num) {
  if (num === 1 || isNaN(num)) return 1;
  return num * fact(num - 1);
}
console.log(fact(num));
