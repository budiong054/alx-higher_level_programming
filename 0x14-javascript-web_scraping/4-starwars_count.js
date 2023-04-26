#!/usr/bin/node
// The script prints the number of movies where the character
// "Wedge Antilles" is present

const request = require('request');
const url = process.argv[2];
// const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
const characterUrl = /18/;

request(url, (err, res, body) => {
  if (err) console.error(err);

  const films = JSON.parse(body).results;

  let count = 0;
  for (const film of films) {
    if (film.characters.some(e => characterUrl.test(e))) {
      count++;
    }
  }
  console.log(count);
});
