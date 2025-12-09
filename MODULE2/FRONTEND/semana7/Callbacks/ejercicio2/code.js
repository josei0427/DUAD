const fs = require('fs');

let words1 = [];
let words2 = [];

const checkSameWords = () => {
    if (words1.length && words2.length) {
        const sameWords = words1.filter(i => words2.includes(i));
        console.log(sameWords);
    }
};

const reviewWords1 = (err, data) => {
    words1 = data.split(/\s+/);
    checkSameWords();
}

const reviewWords2 = (err, data) => {
    words2 = data.split(/\s+/);
    checkSameWords();
}

fs.readFile('text1.txt', 'utf8', reviewWords1);
fs.readFile('text2.txt', 'utf8', reviewWords2);