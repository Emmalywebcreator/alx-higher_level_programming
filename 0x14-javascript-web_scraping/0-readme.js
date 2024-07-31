#!/usr/bin/node

const fs = require('fs');

if (process.argv.length > 2) {

  fs.readFile(process.argv[2], 'utf8', (data, err) => {
    if (err) {
      console.log(err);
    } else {
      console.log(data);
    }
  });
} else {
  console.log('Usage: node script.js <filepath>');
}
