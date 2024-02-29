#include "Arduino.h"
#include "Arduino_FreeRTOS.h"
#include "semphr.h"

SemaphoreHandle_t xSerialSemaphore;

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
        if(xSemaphoreTake(xSerialSemaphore, (TickType_t)5)==pdTRUE){
            Serial.println("Serial OK");
            xSemaphoreGive(xSerialSemaphore);
        }

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

    if(xSerialSemaphore==NULL){
        xSerialSemaphore = xSemaphoreCreateMutex();
        if(xSerialSemaphore!=NULL) xSemaphoreGive(xSerialSemaphore);
    }

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

