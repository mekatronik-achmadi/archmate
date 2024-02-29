#include "Arduino.h"
#include <STM32FreeRTOS.h>


void taskBlink(void *pvParams){
    while (1) {
        digitalWrite(LED_BUILTIN,HIGH);
        vTaskDelay(100/portTICK_PERIOD_MS);
        digitalWrite(LED_BUILTIN,LOW);
        vTaskDelay(100/portTICK_PERIOD_MS);
    }
}

void taskSerial(void *pvParams){
    while (1) {
        Serial.println("Serial OK");
        vTaskDelay(100/portTICK_PERIOD_MS);
    }
}

void setup(void){
    Serial.begin(115200);

    pinMode(LED_BUILTIN,OUTPUT);

    xTaskCreate(taskBlink,
        "Blink",
        configMINIMAL_STACK_SIZE,
        NULL,
        tskIDLE_PRIORITY+1,
        NULL);

    xTaskCreate(taskSerial,
        "Serial",
        configMINIMAL_STACK_SIZE,
        NULL,
        tskIDLE_PRIORITY+2,
        NULL);

    vTaskStartScheduler();
}

void loop(void){
    // should be empty for Arduino FreeRTOS
}

