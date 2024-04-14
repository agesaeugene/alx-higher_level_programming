#!/usr/bin/node
//First two node arguments are removed
const args = process.argv.slice(2);
if (args.length === 0 || isNaN(args[0])) {
	console.log("Missing size");
} else {
  const size = parseInt(args[0]);
  if (size <= 0) {
    console.log("Invalid size");
  } else {
    for (let i = 0; i < size; i++) {
      console.log("X".repeat(size));
    }
  }
}
