
// for(let i=2000; i <= 2021; i++){
//     if (i % 4 === 0 && i % 100 !== 0 || i % 400 === 0)
//     console.log(i)
// }

// function showMessage(num1, num2){
//     let sum = num1 + num2
//     console.log(sum)
// }
// showMessage(2,6)

// let showMessage2 = function(){
//     console.log("asa")
// }
// showMessage2()

// let showMessage3 = () => console.log("asassaaaaaaa")
// showMessage3()

// function calcSum(num1, num2, more, less){
//     let sum = num1 + num2
//     if(sum>=10){
//         more()
//     }
//     else{
//         less()
//     }
// }

// function showMore(){
//     console.log("болье")
// }

// function showLess(){
//     console.log("asdaz")
// }

// calcSum(9, 10, showMore, showLess)

// function showMessage(num1, num2){
//     let sum = num1 + num2
//     return sum
// }
// let a = showMessage(1, 2)
// console.log(a)

// function calcSum(num1, num2){
//     let sum = 1;
//     for(let i = 0; i < num2; i++){
//         sum = num1 * num1
//     }
//     return sum
// }
// console.log(calcSum(5, 6))

function whichIsLowest(num1, num2){
    if(num1>num2){
        console.log(num2)
    }
    else{
        console.log(num1)
    }
}

function raiseToPower(num1, power){
    return num1 = num1 ** power
}

// console.log(raiseToPower(2, 3))

function calculate(num1, num2, sign){
    switch(sign){
        case "+":
            return num1 + num2
            break
        case "-":
            return num1 - num2
            break
        case "*":
            return num1 * num2
            break
        case "/":
            return num1 / num2
            break
        default:
            return "хз"
    }
}

// console.log(calculate(2,3,'-'))


// 4 не надо
// function ifSimple(num1){
//     if(){
//         return "норм"
//     }
//     else{
//         return "не"
//     }
// }

// console.log(ifSimple(2))

// function returnTable(num1){
//     for (let i = 2; i <= 9; i++) {
//         console.log(num1 * i);
//     }
// }

// returnTable(3)

//6 нет