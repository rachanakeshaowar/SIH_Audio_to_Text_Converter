if ("webkitSpeechRecognition" in window) {
  let speechRecognition = new 
  webkitSpeechRecognition();
  let final_transcript = "";
  var speech = true;
  speechRecognition.continuous = true;