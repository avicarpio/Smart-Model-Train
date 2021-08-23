import '/node_modules/blob';
import { saveAs } from '/node_modules/file-saver';

var blob;
var sliderValue = 0;

function writeToFile(){

    sliderValue = document.getElementById("myRange").value; 

    blob = new Blob([sliderValue], {type: "text/plain;charset=utf-8"});

    saveAs(blob, "sliderValue.txt");
}

function infiniteLoop(){
    while(true){
        sleep(20);
        writeToFile();
    }
}

infiniteLoop();