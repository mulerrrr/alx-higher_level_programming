#!/usr/bin/node
// computes the number of tasks completed by user id.
const request = require('request');
const url = process.argv[2];
request(url, 'utf-8', (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const info = JSON.parse(body);
    const taskByUserId = {};
    for (let index = 0; index < info.length; index++) {
      if (info[index].completed && !(info[index].userId in taskByUserId)) {
        taskByUserId[info[index].userId] = 1;
      } else if (info[index].completed && (info[index].userId in taskByUserId)) {
        taskByUserId[info[index].userId] += 1;
      }
    }
    console.log(taskByUserId);
  }
});
