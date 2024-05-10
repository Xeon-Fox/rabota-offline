// let array = [1,2,3,4,5] 
// let index1 = array[0] 
// let [a, b, c] = array 
// console.log(a, b, c) 
 
 
// function calcSum(a,b){ 
//     let newArray = [ 
//         a + b, 
//         a - b, 
//         a * b, 
//         a / b 
//     ] 
//     return newArray 
// } 
// let [a, b, c, d] = (4,5) 
// console.log(a,b,c,d) 
 
 
 
// let array = [1,2,3,4,5] 
// let iterator = array[Symbol.iterator]() 
// console.log(iterator.next()) 
 
 
//// 
 
 
// let array = [1,2,3,4,5] 
// let array2 = [4,5,6,7,8] 
// let allArray = array.concat(array2) 
// let allArray2 = [...array, ...array2] 
// console.log(allArray, allArray2) 
 
 
///// 
 
// let sum = array.reduce((a, i)=> a + i, 0) 
 
// let array = [1,2,3,4,5]

// function CreateMenu(...items){

// }

let user = {
    name: "uias",
    age: 12,
    email: "@sdasd.ru"
}

let {name, age, email} = user
console.log(name, age, email)