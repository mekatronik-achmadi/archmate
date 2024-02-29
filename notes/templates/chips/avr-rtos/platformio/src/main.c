#include "Arduino.h"
#include "Arduino_FreeRTOS.h"

void taskBlink(void *pvParams){
    while (1){
        digitalWrite(LED_BUILTIN,HIGH);
        vTaskDelay(10);
        digitalWrite(LED_BUILTIN,LOW);
        vTaskDelay(10);
    }
}

void setup(void){
    pinMode(LED_BUILTIN,OUTPUT);

    xTaskCreate(taskBlink,
        "Blink",
        32,
        NULL,
        tskIDLE_PRIORITY+1,
        NULL);
}

void loop(void){
    vTaskDelay(10);
}
