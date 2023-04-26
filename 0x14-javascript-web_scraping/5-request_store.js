#!/usr/bin/node
// The script gets the contents of a webpage and stores it in a File

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, (err, res, body) => {
  if (err) console.error(err);
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) console.error(err);
  });
});
