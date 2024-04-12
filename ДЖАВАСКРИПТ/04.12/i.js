let mainForm = document.forms.main
// let mainForm2 = document.forms[1]
// console.log(mainForm, mainForm2)  
let input = mainForm.nameInput
let placeholder = input.placeholder
console.log(input)

input.addEventListener('focus', function(){
    input.placeholder = ""
})
// input.addEventListener("blur", function(){
//     input.placeholder = placeholder
// })

input.addEventListener("blur", function(){
    input.placeholder = placeholder
})