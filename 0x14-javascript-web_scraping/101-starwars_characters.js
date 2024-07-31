#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';

request(url, function (error, response, body) {
	if (error) {
		console.log(error); //prints error incase of an occurence
	} else {
		for (const character of JSON.parse(body).characters) {
			request(character, function (error, response, body) {
				if (error) {
					console.log(error); // prints the error
				} else {
					console.log(JSON.parse(body).name);
				}
			});
		}
	}
});
