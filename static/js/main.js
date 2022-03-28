    // TODO: Add a funstion when submit button clicked to add everything to an array

    $( document ).ready(function() {


    function submitdata() {
        // for (let i = 0; i < {{questions.length}}; i++) {
        //     var a1= document.getElementById("answer-1").value;
        //     console.log(a1);
        // }
        
        let answerList = [];



        var answer= document.getElementById("answer-{{loop.index}}").value;
        answerList.push(answer);

        console.log(answerList);

        // $.post( "/blog/submit_answers", {
        //     user_answers: JSON.stringify(answerList)
        // }, function(err, req, resp){

        //     // window.location.href = "/results/"+resp["responseJSON"];
        //     window.location.href = "/";
        //     console.log(resp);
        // });

    $.post( "{{ url_for('posts.sub') }}", {
      canvas_data: JSON.stringify(answerList)
    }, function(err, req, resp){
    //   window.location.href = "/blog/result/"+resp["responseJSON"];  /results/"+resp["responseJSON"]["unique_id"]
        window.location.href = "/blog/result/"+"hello";
      console.log(resp);
    });

  }

  $( "#sendAnswers" ).click(function(){
        console.log("Yeee");
        submitdata();
  });

});
