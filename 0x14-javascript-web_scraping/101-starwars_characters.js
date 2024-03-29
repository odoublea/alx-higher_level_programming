#!/usr/bin/node
const request = require('request'); const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request(url, (error, response, body) => {
  if (!error) {
    const movies = JSON.parse(body);
    const characters = movies.characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  request(characters[index], (error, response, body) => {
    if (!error) {
      const character = JSON.parse(body);
      console.log(character.name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
