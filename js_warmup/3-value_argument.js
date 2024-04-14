#!/usr/bin/node

// Delete the first two parameters (node and script name).
const args = process.argv.slice(2);

if (args[0]) {
	console.log(args[0]);
} else {
	console.log("No argument");
}
