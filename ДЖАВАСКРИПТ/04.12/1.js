// function FilledAll() {
//     let inputs = document.forms['main'].getElementsByTagName('input')
//     let isEmpty = true
//     for (let i = 0; i < inputs.length; i++) {
//         if (inputs[i].value === '') {
//             isEmpty = false
//             break
//         }
//     }
//     if(isEmpty){
//       alert('заполнил👍')
//     } 
//     else{
//       alert('заполни')
//     }
// }

let mainForm = document.forms[0]
let input = mainForm.nameInput
let button = mainForm.btn

button.addEventListener("click", function(event){
  console.log("норм")
  if(!input.value){
    console.log("ненорм")
    event.preventDefault()
  }
})
