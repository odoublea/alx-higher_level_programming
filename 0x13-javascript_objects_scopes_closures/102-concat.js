#!/usr/bin/node

const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const destFile = process.argv[4];

const data1 = fs.readFileSync(file1, 'utf8');
const data2 = fs.readFileSync(file2, 'utf8');

fs.writeFileSync(destFile, data1 + data2);
