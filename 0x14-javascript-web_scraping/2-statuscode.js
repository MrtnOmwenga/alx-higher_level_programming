#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  else {
    console.log('code:', response.statusCode);
  }
});