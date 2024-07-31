#!/usr/bin/node

const request = require('request');
const fs = require('fs')
const url = process.argv[2];
const path = process.argv[3];
const file = process.argv[4];

request(url, function (error, response, body) {
	if (!error && response.statusCode === 200) {
		fs.writeFile(path + file, body, 'utf8', (err) => {
			if (err) {
				console.log(err);
			}
		});
	}
});
