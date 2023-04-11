#!/usr/bin/node

const { argv } = require('process');
const arg1 = parseInt(argv[2]);
const arg2 = parseInt(argv[3]);

const add = (arg1, arg2) => {
	console.log(arg1 + arg2);
}
add(arg1, arg2);
