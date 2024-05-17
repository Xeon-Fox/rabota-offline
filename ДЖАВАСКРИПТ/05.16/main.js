let input = document.querySelector('#city')
let btn = document.querySelector('#btn')
let img = document.querySelector('.pict')
let city = document.querySelector('.city')
let temp = document.querySelector('.temp')

let sunny_pict = 'May-16\sunny.png'
let clouds_pict = 'May-16\cloudy.png'
let rain_pict = 'May-16\windy.png'
let snow_pict = 'May-16\snowy.png'

let API_KEY = 'cc2d757656721c7838f819f150c7f7e6'


btn.addEventListener('click', async function(){
    let API_URL = 'https://api.openweathermap.org/data/2.5/weather?q=${input.value}&appid=${API_KEY}'

    let res = await fetch(API_URL)
    let data = await res.json()
    if('main' in data){
        console.log(data)
    }
})