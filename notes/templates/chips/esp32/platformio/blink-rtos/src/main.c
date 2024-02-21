#include <esp_system.h>
#include <esp_console.h>
#include <esp_vfs_dev.h>
#include <esp_err.h>

#include <freertos/FreeRTOS.h>
#include <freertos/task.h>

#include <driver/gpio.h>
#include "driver/uart.h"

#define BLINK_GPIO  2
#define BLINK_DELAY 100

#define CONFIG_ESP_CONSOLE_UART_NUM 0

static void ledTask(void *pvParameter){
    gpio_set_level(BLINK_GPIO,1);

    while (1) {
        gpio_set_level(BLINK_GPIO,0);
        vTaskDelay(BLINK_DELAY / portTICK_PERIOD_MS);

        gpio_set_level(BLINK_GPIO,1);
        vTaskDelay(BLINK_DELAY / portTICK_PERIOD_MS);
    }
}

static void uartTask(void *pvParameter){
    while (1) {
        printf("Serial OK\n");
        vTaskDelay(BLINK_DELAY / portTICK_PERIOD_MS);
    }
}

static void uart_Init(void){
fflush(stdout);
    fsync(fileno(stdout));
    setvbuf(stdin,NULL,_IONBF,0);

    esp_vfs_dev_uart_port_set_rx_line_endings(CONFIG_ESP_CONSOLE_UART_NUM,
            ESP_LINE_ENDINGS_CR);
    esp_vfs_dev_uart_port_set_tx_line_endings(CONFIG_ESP_CONSOLE_UART_NUM,
            ESP_LINE_ENDINGS_CRLF);

    const uart_config_t uart_Conf = {
        .baud_rate = 115200,
        .data_bits = UART_DATA_8_BITS,
        .parity = UART_PARITY_DISABLE,
        .stop_bits = UART_STOP_BITS_1,
        .source_clk = UART_SCLK_REF_TICK
    };

    uart_driver_install(CONFIG_ESP_CONSOLE_UART_NUM,
            256,
            0,
            0,
            NULL,
            0);

    uart_param_config(CONFIG_ESP_CONSOLE_UART_NUM,&uart_Conf);
    esp_vfs_dev_uart_use_driver(CONFIG_ESP_CONSOLE_UART_NUM);
}

void app_main() {
    gpio_reset_pin(BLINK_GPIO);
    gpio_set_direction(BLINK_GPIO,GPIO_MODE_OUTPUT);

    uart_Init();

    xTaskCreate(&ledTask,
            "LED-Task",
            1024,
            NULL,
            tskIDLE_PRIORITY+1,
            NULL);

    xTaskCreate(&uartTask,
            "UART-Task",
            2048,
            NULL,
            tskIDLE_PRIORITY+1,
            NULL);

}
