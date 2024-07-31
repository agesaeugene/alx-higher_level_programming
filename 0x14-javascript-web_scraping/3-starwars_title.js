#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/';
request(url, function (error, response, body) {
  if (error) {
    console.log(error); // Prints the error in the event one occured
  } else {
    console.log(JSON.parse(body).title); // Print the response status code in the event a response was received
  }
});
