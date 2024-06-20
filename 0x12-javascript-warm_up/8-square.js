#!/usr/bin/node
const sqr_size = parseInt(process.argv[2]);
if (isNaN(sqr_size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sqr_size; i++) {
    let row = '';
    for (let j = 0; j < sqr_size; j++) {
	row += 'X';
    }
    console.log(row);
  }
}
