#!/usr/bin/node
const request = require('request'); const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endwith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
