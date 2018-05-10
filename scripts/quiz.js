function check() {
  var answer = document.getElementById('answer')
  console.log(document.quiz)
  var q1 = document.quiz.q1.value
  var q2 = document.quiz.q2.value

  var correct = 0

  if (q1 == '1') {
    correct++
  }
  if (q2 == '1') {
    correct++
  }
  answer.innerHTML = 'Your scor is: ' + correct * 100 / 2
}
