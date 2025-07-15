fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
.then((data) => {
    console.log(data.json());
    /*document.getElementById("name")*/
})