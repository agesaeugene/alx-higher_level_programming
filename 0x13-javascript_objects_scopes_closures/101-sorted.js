#!/usr/bin/node
const dict = require('./101-data').dict;

const newdict = {};
let list = [];
for (const [key, value] of Object.entries(dict)) {
	  if (!(value in newdict)) {
		      list = [];
		    } else {
			        list = newdict[value];
			      }
	  list.push(key);
	  newdict[value] = list;
}
console.log(newdict);
