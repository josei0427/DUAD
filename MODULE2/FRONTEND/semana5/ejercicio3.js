const myTempC = [27, 19, 30, 22, 32];
let myTempF = myTempC.map(function(i){
    return (i * 9 / 5) + 32
})

console.log(myTempF)