function getPokemon(id) {
    return fetch(`https://pokeapi.co/api/v2/pokemon/${id}`)
    .then(res => res.json());
}
Promise.all([getPokemon(2), getPokemon(4), getPokemon(8)])
.then(results => {
    console.log("The 3 pokemons are:");
    console.log(results[0].name);
    console.log(results[1].name);
    console.log(results[2].name);
})
.catch(err => console.error("Error:", err));