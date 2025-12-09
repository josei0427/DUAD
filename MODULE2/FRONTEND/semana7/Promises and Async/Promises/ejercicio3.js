const myList = ["very", "dogs", "cute", "are"];

function getWords(theWord) {
    return new Promise((resolve) => {
        setTimeout(() =>{
            resolve(theWord);
        }, 1000);
    });
}

Promise.all([getWords(myList[1]), getWords(myList[3]), getWords(myList[0]), getWords(myList[2])])
.then(results => {
    console.log("The actual phrase is: ");
    console.log(results.join(" "));
})
.catch(err => console.error("Error:", err));