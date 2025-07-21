// const myArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
// let mySecArray = [];
// for (let i = 0; i < myArray.length; i++) {
//     if (myArray[i] % 2 === 0){
//         mySecArray.push(myArray[i])
//     }
// }
// console.log(mySecArray)


const myArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
let mySecArray = myArray.filter(function(i){
    return i % 2 === 0;
});
console.log(mySecArray)