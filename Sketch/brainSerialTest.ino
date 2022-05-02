
#include <Brain.h>

// Set up the brain parser, pass it the hardware serial object you want to listen on.
Brain brain(Serial);

void setup() {
    // Start the hardware serial.
    Serial.begin(9600);
}

void loop() {
    // Expect packets about once per second.
    // The .readCSV() function returns a string (well, char*) listing the most recent brain data, in the following format:
    // "signal strength, attention, meditation, delta, theta, low alpha, high alpha, low beta, high beta, low gamma, high gamma"
    if (brain.update()) {
        //Serial.println(brain.readErrors());
        //Serial.println(brain.readCSV());
        //Serial.println(brain.readAttention());
        //Serial.println(brain.readSignalQuality());
        //Serial.println(brain.readSignalQuality());
        //Serial.println(brain.readLowBeta());

        String signalQuality = String(brain.readSignalQuality());
        String attention = String(brain.readAttention());
        Serial.println(signalQuality + "," + attention);
    }

  //print out attention greater than or equal to 20

}
