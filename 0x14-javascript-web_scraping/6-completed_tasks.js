#!/usr/bin/node
// The script computes the number of tasks
// completes by user id

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) console.error(err);
  const json = JSON.parse(body);
  const obj = {};
  for (let i = 1; i <= 10; i++) {
    let completeTask = 0;
    for (const todo of json) {
      // console.log(todo);
      if (todo.userId === i && todo.completed) {
        completeTask++;
      }
    }
    obj[i] = completeTask;
  }
  console.log(obj);
});
