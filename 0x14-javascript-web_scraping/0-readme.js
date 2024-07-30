#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
	if (err) {
		consoole.log(err);
	} else {
		console.log(data);
	}
});

const args = process.argv.slice(2);
if (args.length !== 1) {
    console.log('Usage: node script.js <file_path>');
} else {
    readFile(args[0]);
}

