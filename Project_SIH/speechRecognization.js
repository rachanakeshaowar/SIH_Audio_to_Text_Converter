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








