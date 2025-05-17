if ("webkitSpeechRecognition" in window) {
  let speechRecognition = new 
  webkitSpeechRecognition();
  let final_transcript = "";
  var speech = true;
  speechRecognition.continuous = true;
   speechRecognition.interimResults = true;
  speechRecognition.lang = document.querySelector("#select_dialect").value;
  speechRecognition.onstart = () => {
     document.querySelector("#status").style.display = "block";
  };
  speechRecognition.onerror = () => {
    document.querySelector("#status").style.display = "none";
     console.log("Speech Recognition Error");
  };
  speechRecognition.onend = () => {
    if (speech === true) {
      speechRecognition.start();
    }
    console.log(speech, 'dd')
    document.querySelector("#status").style.display = "none";
     console.log("Speech Recognition Ended");
  };
  speechRecognition.onresult = (event) => {
    let interim_transcript = "";
    or (let i = event.resultIndex; i < event.results.length; ++i) {
      if (event.results[i].isFinal) {
        final_transcript += event.results[i][0].transcript;
         } else {
        interim_transcript += event.results[i][0].transcript;
         }
    }
 document.getElementById('final').innerHTML = final_transcript;
 document.querySelector("#interim").innerHTML = interim_transcript;
   };
    document.querySelector("#start").onclick = () => {
       speechRecognition.start();
  };
    document.getElementById('stop').
    addEventListener('click', e => {
      speechRecognition.removeEventListener("end", speechRecognition.start);
      speechRecognition.stop();
    







































