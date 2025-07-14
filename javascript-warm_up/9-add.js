#!/usr/bin/node
function isNumeric (str) {
  if (typeof str !== 'string') return false; // we only process strings!
  return !isNaN(str) && // use type coercion to parse the _entirety_ of the string (`parseFloat` alone does not do this)...
         !isNaN(parseFloat(str)); // ...and ensure strings of whitespace fail
}

function add (a, b) {
  console.log(parseFloat(a) + parseFloat(b));
}

if (isNumeric(process.argv[2]) && isNumeric(process.argv[3])) { add(process.argv[2], process.argv[3]); } else { console.log('NaN'); }
