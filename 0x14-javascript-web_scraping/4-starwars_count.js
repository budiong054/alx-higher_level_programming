#!/usr/bin/node
// The script prints the number of movies where the character
// "Wedge Antilles" is present

const request = require('request');
const url = process.argv[2];
const people_url = "https://swapi-api.alx-tools.com/api/people/18/"

request(url, (err, res, body) => {
	if (err) console.error(err);

	const film_json = JSON.parse(body);
	const array = film_json['results'].filter(el => {
		console.log(el['characters'].includes(people_url) === true);
	});
	console.log(array);
});
