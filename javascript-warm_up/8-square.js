#!/usr/bin/node
function isNumeric (str) {
  if (typeof str !== 'string') return false; // we only process strings!
  return !isNaN(str) && // use type coercion to parse the _entirety_ of the string (`parseFloat` alone does not do this)...
         !isNaN(parseFloat(str)); // ...and ensure strings of whitespace fail
}

function boucle () {
  let str = '';
  for (let step = 0; step < process.argv[2]; step++) {
    // Runs 5 times, with values of step 0 through 4.
    str += 'X';
  }

  for (let step = 0; step < process.argv[2]; step++) {
    // Runs 5 times, with values of step 0 through 4.
    console.log(str);
  }
}

if (isNumeric(process.argv[2])) { boucle(); } else { console.log('Missing size'); }
