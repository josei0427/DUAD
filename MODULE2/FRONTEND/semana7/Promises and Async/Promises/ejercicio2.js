function getPokemon(id) {
    return fetch(`https://pokeapi.co/api/v2/pokemon/${id}`)
    .then(res => res.json());
}
Promise.any([getPokemon(2), getPokemon(4), getPokemon(8)])
.then(results => {
    console.log("The pokemons is:");
    console.log(results.name);
})
.catch(err => console.error("Error:", err));