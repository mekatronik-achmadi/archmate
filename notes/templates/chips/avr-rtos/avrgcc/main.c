#include <avr/io.h>

#include "FreeRTOS.h"
#include "task.h"

void taskBlink(void *pvParams){

    const portTickType xFreq = 100;
    portTickType xWakeTime = xTaskGetTickCount();

    while (1) {
        PORTB ^= 1<<5;
        vTaskDelayUntil(&xWakeTime,xFreq);
    }
}

int main(void)
{

    DDRB |= 1<<5;
    PORTB |= 1<<5;

    xTaskCreate(taskBlink,
            "Blink",
            configMINIMAL_STACK_SIZE,
            NULL,
            tskIDLE_PRIORITY+1,
            NULL);

    vTaskStartScheduler();

    return 0;
}

void vApplicationIdleHook(void){
    // empty for now
}

