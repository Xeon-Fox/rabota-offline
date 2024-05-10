function checkAnswers() {
    let correctAnswers = 0
    let totalQuestions = 2
  
    let answer1 = document.getElementById('answer1').checked
    let answer2 = document.getElementById('answer2').checked
    let answer3 = document.getElementById('answer3').checked
    let answer4 = document.getElementById('answer4').checked
  
    if (answer1) {
      correctAnswers++
    }
  
    else if (!answer2) {
      correctAnswers++
    }
  
    if (!answer3) {
      correctAnswers++
    }
  
    else if (answer4) {
      correctAnswers++
    }
    alert(`${correctAnswers} правильных из ${totalQuestions}`)
  }
  