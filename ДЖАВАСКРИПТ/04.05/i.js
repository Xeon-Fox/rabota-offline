// let now = new Date()
// console.log(getDate(now))

// function sendMessage(){
//     console.log("saasdd")
// }
// setTimeout(sendMessage, 2000)

// setTimeout(function hello(){
//     setTimeout(() => {
//         console.log("world")
//     }, 3000);
//     console.log("hi")
// }, 3000)

// try{
//     setTimeout(function hello(){
//         setTimeout(() => {
//             console.log("го кахут")
//         }, 3000);
//         console.log("пж")
//     }, 3000)
//     z;
// }
// catch(error){
//     console.log(error.name)
//     console.log(error.message)
// }
// finally{
//     console.log("урра работает")
// }




// let text = document.getElementById("text")
// text.textContent = 'hiiiii'
// text.innerHTML = 'hiiiii'
// text.style.color = "red"

// let z = document.getElementById("z")
// let v = document.getElementById("v")
// let o = document.getElementById("o")
// z.style.fontStyle = "bold"
// v.style.fontStyle = "italic"
// o.style.textDecoration = "underline"

colorbase = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']
num = Math.floor(Math.random() * 7);
color = colorbase[num]
let z = document.getElementById("z")
z.style.color = color


fontsize = Math.floor(Math.random() * 256);
console.log(fontsize)
z.style.fontSize = fontsize + 'px'