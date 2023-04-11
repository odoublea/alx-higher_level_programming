#!/usr/bin/node
const { argv } = require('process');
const arg = parseInt(argv[2]);

if (isNaN(arg)) {
	console.log(`Not a Number`);
} else {
	console.log(`My number: ${arg}`);
}
