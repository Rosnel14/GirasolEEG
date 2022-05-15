
#include <Brain.h>

// Set up the brain parser, pass it the hardware serial object you want to listen on.
Brain brain(Serial);

void setup() {
    // Start the hardware serial.
    Serial.begin(9600);
}

void loop() {
    // Expect packets about once per second.
    if (brain.update()) {

      //For general use 
        String signalQuality = String(brain.readSignalQuality());
        String attention = String(brain.readAttention());
        String gamma = String(brain.readLowGamma());
        String endbit = String(0);   
        Serial.println(signalQuality + "," + attention + "," + gamma + "," + endbit); 
    }

  
  
}
