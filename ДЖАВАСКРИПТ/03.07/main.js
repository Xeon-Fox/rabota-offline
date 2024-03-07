// let age = +prompt("asdasd ")
// if(age>=0 && age<=19){
//     console.log("1")
// }
// else if(age>=9 && age<15){
//     console.log("2")
// }
// else{
//     console.log("старина съеби нахуй")
// }

// let color = prompt("Color")

// switch(color){
//     case "yellow":
//         console.log("ASdasdxcvxcvxcvzxcvzxc")
//     break;
//     case "red":
//         console.log("ZZZZZZZZZZ")
//     break;
//     case "green":
//         console.log("kghjolmghkjv")
//     break;
//     default:
//         console.log("jb uibnf[gphkdr")
//     break;
// }

// console.log(5 == "5")
// console.log(5 === "5")

// let t = +prompt("time")
// if(t > 23 || t< 9){
//     console.log("zakrit")
// }
// else{
//     console.log(`asdjasd na: ${t}`)
// }



// let a = +prompt("Asdasd")
// if(a>0){
//     alert("hu")
// }
// else if(a===0){
//     alert("asjghsd")
// }
// else{
//     alert("😋")
// }


// let a = +prompt("Asdasd")
// if(a>=0 || a<=120){
//     alert("hu")
// }
// else{
//     alert("😋")
// }

// let a = +prompt("Asdasd")
// alert(Math.abs(a))


// let a = +prompt("Asdasd")
// let b = +prompt("Asdasd")
// let c = +prompt("Asdasd")
// if(a<=24 && b<60 && c<60){
//     alert("hu")
// }
// else{
//     alert("😋")
// }

// let x = +prompt("Asdasd")
// let y = +prompt("Asdasd")
// if(x>0 && b>0){
//     alert("1")
// }
// if(x>0 && y<0){
//     alert("4")
// }
// if(x<0 && y>0){
//     alert("2")
// }
// if(x<0 && y<0){
//     alert("3")
// }
// else{
//     alert("фигня")
// }

// let z = +prompt("ASd")
// switch (z) {
//     case "1":
//         console.log("Январь");
//         break;
//     case "2":
//         console.log("Февраль");
//         break;
//     case "3":
//         console.log("Март");
//         break;
//     case "4":
//         console.log("Апрель");
//         break;
//     case "5":
//         console.log("Май");
//         break;
//     case "6":
//         console.log("Июнь");
//         break;
//     case "7":
//         console.log("Июль");
//         break;
//     case "8":
//         console.log("Август");
//         break;
//     case "9":
//         console.log("Сентябрь");
//         break;
//     case "10":
//         console.log("Октябрь");
//         break;
//     case "11":
//         console.log("Ноябрь");
//         break;
//     case "12":
//         console.log("Декабрь");
//         break;
//     default:
//         console.log("Неверный номер месяца");
//     break;
// }

// let num1 = +prompt("asd ")
// let num2 = +prompt("asd ")
// let operation = +prompt("asd ")

// switch (operation) {
//     case "+":
//         console.log(num1 + num2) 
//         break;
//     case "-":
//         console.log(num1 - num2) 
//         break;
//     case "*":
//         console.log(num1 * num2)
//         break;
//     case "/":
//         console.log(num1 / num2) 
//         break;
//     default:
//         console.log("Неверная операция");

let element = +prompt("kas")

switch (typeof element){
    case "string":
        console.log("Строка") 
    break;
    case "number":
        console.log("Число") 
    break;
    case "boolean":
        console.log("Булево значение")
    break;
    default:
        console.log("хз")
    break;
}