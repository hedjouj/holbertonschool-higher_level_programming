const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const character = document.querySelector('#character');

fetch(url).then((response) => {
  return response.json();
}).then((data) => {
  character.textContent = data.name;
});