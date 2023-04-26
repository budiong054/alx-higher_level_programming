#!/usr/bin/node
// The script prints all characters of a Star Wars movie

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, (err, res, body) => {
  if (err) console.error(err);

  const characters = JSON.parse(body).characters;

  for (const characterUrl of characters) {
    request(characterUrl, (err, res, body) => {
      if (err) console.error(err);
      console.log(JSON.parse(body).name);
    });
  }
});
