#!/usr/bin/node
let max1 = parseFloat(process.argv[2]);
let max2 = parseFloat(process.argv[3]);
if (parseFloat(process.argv[2]) < parseFloat(process.argv[3])) {
  max1 = parseFloat(process.argv[3]);
  max2 = parseFloat(process.argv[2]);
}

for (let i = 4; i < process.argv.length; i++) {
  if (parseFloat(process.argv[i]) < max1 && parseFloat(process.argv[i]) > max2) {
    max2 = parseFloat(process.argv[i]);
  } else if (parseFloat(process.argv[i]) > max1) {
    max2 = max1;
    max1 = parseFloat(process.argv[i]);
  }
}
if (process.argv.length > 3) { console.log(max2); } else { console.log('0'); }
