const mySentence = "This is a message";
let myArray = [];
let cWord = "";
for (let i = 0; i < mySentence.length; i++){
    if (mySentence[i] !== " "){
        cWord += mySentence[i]
    }
    else{
        if (cWord !== ""){
            myArray.push(cWord)
            cWord = "";
        }
    }
}
if (cWord !== "") {
    myArray.push(cWord);
}
console.log(myArray);