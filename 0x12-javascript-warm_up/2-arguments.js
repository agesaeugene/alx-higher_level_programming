#!/usr/bin/node


//(node and first two elements of the code are removed
const args = process.argv.slice(2);


if (args.length === 0) {
  console.log("No argument");
} else if (args.length === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}


