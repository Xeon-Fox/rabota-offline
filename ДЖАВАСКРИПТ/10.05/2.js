document.querySelector('#inputbtn').addEventListener('click', () =>{ 
    let text = document.querySelector('#input').value
    let request = new XMLHttpRequest() 
    request.open('GET', `https://restcountries.com/v3.1/name/${text}`)
    request.onload = () =>  {
      let a = JSON.parse(request.response)
      let c = a[0]
      let of = c.name.official
      let population = c.population
      let region = c.subregion
      let flag = c.flags.alt
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

document.querySelector('#mapbtn').addEventListener('click', () => {
    let text = document.querySelector('#input').value
    let request = new XMLHttpRequest() 
    request.open('GET', `https://restcountries.com/v3.1/name/${text}`)
    request.onload = () =>  {
        let a = JSON.parse(request.response)
        let c = a[0]
        link = c.maps.googleMaps
        let modal = document.getElementById("modal");
        let openButton = document.querySelector("#mapbtn");
        openButton.addEventListener("click", () => {
            modal.style.display = "block";
        });
        document.getElementById("map").src= link;
    }
    request.send()
})