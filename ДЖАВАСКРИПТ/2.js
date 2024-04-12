// let mainForm = document.forms.main
// let input = mainForm.nameinput
// input.addEventListener("copy", function(event){
//     console.log("copy")
// })
// input.addEventListener("paste", function(event){
//     console.log("paste")
//     event.preventDefault()
// })
// input.addEventListener("cut", function(event){
//     console.log("cut")
// })

let mainForm = document.forms.main 
let mainFormSelect = mainForm.nameSelect 
 
console.log(mainFormSelect.options) 
 
let mainFormSelectIndex = mainFormSelect.selectedIndex 
console.log(mainFormSelectIndex) 
 
let mainFormSelectValue = mainFormSelect.value 
console.log(mainFormSelectValue) 
 
let mainFormSelectText = mainFormSelect.options[mainFormSelectIndex].text 
console.log(mainFormSelectText)