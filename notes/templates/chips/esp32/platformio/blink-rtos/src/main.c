#include <esp_system.h>
#include <esp_console.h>
#include <esp_vfs_dev.h>
#include <esp_err.h>

#include <freertos/FreeRTOS.h>
#include <freertos/task.h>

#include <driver/gpio.h>
#include <driver/uart.h>

#include "shell.h"

#define BLINK_GPIO  2
#define BLINK_DELAY 100

static void ledTask(void *pvParameter){
    gpio_set_level(BLINK_GPIO,1);

    while (1) {
        gpio_set_level(BLINK_GPIO,0);
        vTaskDelay(BLINK_DELAY / portTICK_PERIOD_MS);

        gpio_set_level(BLINK_GPIO,1);
        vTaskDelay(BLINK_DELAY / portTICK_PERIOD_MS);
    }
}

void app_main() {
    gpio_reset_pin(BLINK_GPIO);
    gpio_set_direction(BLINK_GPIO,GPIO_MODE_OUTPUT);

    shell_Init();

    xTaskCreate(&ledTask,
            "LED-Task",
            1024,
            NULL,
            tskIDLE_PRIORITY+1,
            NULL);

    while (1) {
        int shell = shell_Loop();
        if(shell==1) break;

        vTaskDelay(1/portTICK_PERIOD_MS);
    }
}
