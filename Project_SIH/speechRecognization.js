if ("webkitSpeechRecognition" in window) {
  let speechRecognition = new 
  webkitSpeechRecognition();
  let final_transcript = "";
  var speech = true;
  speechRecognition.continuous = true;
   speechRecognition.interimResults = true;
  speechRecognition.lang = document.querySelector("#select_dialect").value;
  speechRecognition.onstart = () => {




    