#!/usr/bin/node
const sqrSize = parseInt(process.argv[2]);
if (isNaN(sqrSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sqrSize; i++) {
    let row = '';
    for (let j = 0; j < sqrSize; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
