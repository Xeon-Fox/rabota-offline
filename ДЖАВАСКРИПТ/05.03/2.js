// let obj1 = { 
//     name: 'Alex', 
//     age: 25, 
//     email: 'alex02@mail.ru' 
// } 
 
// console.log(obj1) 
// let obj2 = JSON.stringify(obj1, null, 3) 
// console.log(obj2) 
// let obj3 = JSON.parse(obj2) 
// console.log(obj3) 
 
 
// let request = new XMLHttpRequest() 
// request.open('GET', 'https://api.openweathermap.org/data/2.5/weather?q=Almaty&units=metric&APPID=b03a2cfad336d11bd9140ffd92074504') 
// request.send() 
 
 
// const xhr = new XMLHttpRequest() 
 
// xhr.open('GET', 'https://api.github.com/users/dan') 
// xhr.onload = () => { 
//     console.log(xhr) 
// } 
 
 
// document.querySelector('#btn').onclick = () =>{ 
//     let text = document.querySelector('#text').value 
//     let request = new XMLHttpRequest() 
//     request.open('GET', 'https://api.github.com/users/${text}') 
//     request.onload = () =>  
//         console.log(text) 
// }

document.querySelector('#btn').addEventListener('click', () =>{ 
    let text = document.querySelector('#text').value
    console.log(text); 
    let request = new XMLHttpRequest() 
    request.open('GET', `https://api.openweathermap.org/data/2.5/weather?q=${text}&units=metric&APPID=b03a2cfad336d11bd9140ffd92074504`) 
    request.onload = () =>  
        console.log(request) 
        request.send()
})
// document.querySelector('#btn').onclick = ()=>{
//     let text = document.querySelector('#text')
//     console.log(text);
// }