#!/usr/bin/node
function isNumeric (str) {
  if (typeof str !== 'string') return false; // we only process strings!
  return !isNaN(str) && // use type coercion to parse the _entirety_ of the string (`parseFloat` alone does not do this)...
         !isNaN(parseFloat(str)); // ...and ensure strings of whitespace fail
}

function factorial (value) {
  if (value === 1) { return 1; } else { return value * factorial(value - 1); }
}

if (isNumeric(process.argv[2])) { console.log(factorial(process.argv[2])); } else { console.log('1'); }
