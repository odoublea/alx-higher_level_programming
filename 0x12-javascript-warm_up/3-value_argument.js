#!/usr/bin/node
const { argv } = require('process');
const value = argv[2];

if (!value) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
