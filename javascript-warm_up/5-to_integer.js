#!/usr/bin/node
function isNumeric (str) {
  if (typeof str !== 'string') return false; // we only process strings!
  return !isNaN(str) && // use type coercion to parse the _entirety_ of the string (`parseFloat` alone does not do this)...
         !isNaN(parseFloat(str)); // ...and ensure strings of whitespace fail
}

if (isNumeric(process.argv[2])) { console.log('My number: ' + process.argv[2]); } else { console.log('Not a number'); }
