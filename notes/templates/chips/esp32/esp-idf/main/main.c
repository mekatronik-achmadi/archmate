#include <freertos/FreeRTOS.h>
#include <freertos/task.h>

#include "blink.h"
#include "shell.h"

void app_main(void){
    nvs_Init();
    led_Init();

    shell_Init();

    while (1) {
        int shell = shell_Loop();
        if(shell==1) break;

        vTaskDelay(1/portTICK_PERIOD_MS);
    }
}
