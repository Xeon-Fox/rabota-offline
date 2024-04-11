// let button = document.getElementById("btn")

// function showMessage(){
//     console.log("h")
// }

// button.onclick = function(){
//     console.log('h')
// }

// button.addEventListener("click", function showMessage(){
//     console.log("h")
//     button.removeEventListener("click", showMessage)
// })

// button.addEventListener("click", function(event){
//     console.log(event.type)
//     console.log(event.target)
// })



// div.addEventListener("mousemove", function(event){
//     let x = clientX
//     let y = clientY

//     div.style.left = x + 'px'
//     div.style.top = y + "px"
// })

// let container = document.getElementById("container")
// let close = document.getElementById("close").addEventListener
// ("click", function(){
//     container.style.display = "none"
// })
// let button = document.getElementById("btn").addEventListener
// ("click", function(){
//     container.style.display = "block"
// })   

window.addEventListener("scroll", function(){
    let scrolly = this.window.pageYOffset|| document.documentElement.scrolly
    let layer = this.document.getElementById("layer")

    layer.style.transform = translateY(+scroll*0.5 + "px")
})