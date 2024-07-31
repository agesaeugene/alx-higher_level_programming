#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error); // Prints the error if it occurred
  } else {
    console.log('code:', response && response.statusCode); // Print the response status code upon receiving a response
  }
});
