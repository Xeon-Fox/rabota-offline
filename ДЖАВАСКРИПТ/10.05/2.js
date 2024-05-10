document.querySelector('#inputbtn').addEventListener('click', () =>{ 
    let text = document.querySelector('#input').value
    let request = new XMLHttpRequest() 
    request.open('GET', `https://restcountries.com/v3.1/name/${text}`)
    request.onload = () =>  {
      let a = JSON.parse(request.response)
      let c = a[0]
      console.log(a)
      let of = c.name.official
      let population = c.population
      let region = c.subregion
      let flag = c.flags.alt
      let img = c.flags.png
      console.log(img);
      let img1 = document.querySelector('img')
      img1.src = img
      let p = document.getElementById('info1')
      p.textContent = of
      let p1 = document.getElementById('info2')
      p1.textContent = population
      let p2 = document.getElementById('info3')
      p2.textContent = region
      let p3 = document.getElementById('info4')
      p3.textContent = flag
    }
        request.send()
})

document.querySelector('#fvbtn').addEventListener('click', () => {
    let input = document.querySelector('#input'); 
    let list = document.querySelector('ul'); 

    let text = input.value;
    let newItem = document.createElement('li'); 
    newItem.textContent = text; 

    list.appendChild(newItem);
})