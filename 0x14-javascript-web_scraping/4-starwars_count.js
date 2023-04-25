#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    let count = 0;
    const results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      if (results[i].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    }

    console.log(count);
  }
});
