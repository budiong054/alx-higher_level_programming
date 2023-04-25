#!/usr/bin/node
// This script reads and prints the content of a file

const fs = require('fs');
const file = process.argv[2];

if (file) {
	fs.readFile(file, 'utf-8', (err, data) => {
		if (err) console.error(err);
		console.log(data);
	});
}
