function getNumber(number, fucntion1, function2){
    if (number % 2 === 0){
        fucntion1();
    }
    else{
        function2();
    }
}

function thisIsEven(){
    console.log("This number is even!");
}

function thisIsOdd(){
    console.log("This number is odd!");
}

getNumber(10, thisIsEven, thisIsOdd);