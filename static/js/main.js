window.onload = function(){ 



// Get the button and container elements from HTML:
const button = document.getElementById("sendAnswers");
const data = document.getElementById("info");

// Create an event listener on the button element:
button.onclick= function(){
 // Get the reciever endpoint from Python using fetch:
 
 console.log(q1);
 let answerList = [];
 let subans = [];
  for (let i = 1; i < 999; i++) {
    try {
      var q1 = document.getElementById("qOrder-".concat(i)).innerHTML;
      var a1 = document.getElementById("answer-".concat(i)).value;
      subans.push(q1,a1);
      // console.log(a1);
      answerList.push(subans);
      subans = [];
    }
    catch(err) {
      i = 99999999;
      console.log("error")
    }
  }


  console.log(answerList);

 fetch("http://127.0.0.1:5000/blog/receiver", 
 {
 method: 'POST',
 headers: {
 'Content-type': 'application/json',
 'Accept': 'application/json'
 },
 // Strigify the payload into JSON:
 body:JSON.stringify(answerList)}).then(res=>{
 if(res.ok){
 return res.json()
 }else{
 alert("something is wrong")
 }
 }).then(jsonResponse=>{

 // Log the response data in the console
//  console.log(jsonResponse.score)
  score = jsonResponse.score;
  isCorr = jsonResponse.isCorrect;
  answerList = jsonResponse.answerList;
  percentage = jsonResponse.percentage;



  for (let i = 1; i < 999; i++) {
    try {
      var card = document.getElementById("cardQuestion-".concat(i));
      var input = document.getElementById("answer-".concat(i));

      input.disabled = true;
      card.classList.remove('border-primary');
      if(isCorr[i-1] == true){
        card.classList.add('border-success');
        input.classList.add('is-valid');
      }else{
        card.classList.add('border-danger');
        input.classList.add('is-invalid');
      }
    }
    catch(err) {
      i = 99999999;
      // console.log("error")
    }
  }
  window.scrollTo(0, 0);

  var submitButton = document.getElementById("sendAnswers");
  submitButton.classList.add('disabled');

  // Show score. 
  document.getElementById("scoreDisplay").innerHTML = "Well Done! You got " + jsonResponse.score +  " questions correct";
  document.getElementById("percentageDisplay").innerHTML = "You got " + jsonResponse.percentage + "% !";
 }).catch((err) => console.error(err));

 }

};