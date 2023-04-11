#!/usr/bin/node

const arg = parseInt(process.argv[2]);
const printSquare = (size) => {
  const row = 'X'.repeat(size);
    for (let i = 0; i < arg; i++) {
      console.log(row);
    }
  }

if (Number.isInteger(arg)) {
	printSquare(arg);
} else {
  console.log('Missing size');
}
