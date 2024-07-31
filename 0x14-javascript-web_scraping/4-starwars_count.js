#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, function (error, response, body) {
	if (error) {
		console.log(error);// prints an error in the event one occured
	} else {
	  for (const film of JSON.parse(body).results) {
		  for (const character of film.characters) {
			  if (character.includes('18')) {
				  count++;
			  }
		  }
	  }
		console.log(count);
	  }
});
