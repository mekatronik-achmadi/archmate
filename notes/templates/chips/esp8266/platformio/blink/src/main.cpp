#include <Arduino.h>

#define BLINK_LED 16
#define BLINK_LED2 2

void setup(){
    Serial.begin(115200);
    pinMode(BLINK_LED,OUTPUT);
    pinMode(BLINK_LED2,OUTPUT);
}

void loop(){
    digitalWrite(BLINK_LED, HIGH);
    digitalWrite(BLINK_LED2, LOW);
    delay(200);
    digitalWrite(BLINK_LED, LOW);
    digitalWrite(BLINK_LED2, HIGH);
    delay(200);

    Serial.println("Serial OK");
}
