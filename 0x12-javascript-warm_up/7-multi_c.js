#!/usr/bin/node

const arg = parseInt(process.argv[2]);
const printC = (value) => {
  while (value > 0) {
    console.log('C is fun');
    value--;
  }
};
if (Number.isInteger(arg)) {
  printC(arg);
} else {
  console.log('Missing number of occurrences');
}
