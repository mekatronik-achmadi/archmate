#include "ch.h"
#include "hal.h"

#include "chprintf.h"
#include "shell.h"

#define SHELL_WA_SIZE   THD_WORKING_AREA_SIZE(512)

static THD_WORKING_AREA(waLED,128);
static THD_FUNCTION(thdLED,arg){
    (void) arg;
    chRegSetThreadName("led-blink");
    while (true) {
        palTogglePad(GPIOC,13);
        chThdSleepMilliseconds(100);
    }
}

static thread_t *shelltp = NULL;

static void cmd_test(BaseSequentialStream *chp, int argc, char *argv[]){
    (void) argv;
    if(argc>0) {
        chprintf(chp,"Usage: test\r\n");
        return;
    }

    chprintf(chp,"Serial OK\r\n");
    return;
}

static const ShellCommand sh_cmd[] = {
    {"test",cmd_test},
    {NULL,NULL}
};

static const ShellConfig sh_cfg = {
    (BaseSequentialStream*) &SD1,
    sh_cmd
};

int main(void){
    halInit();
    chSysInit();

    palSetPadMode(GPIOC,13,PAL_MODE_OUTPUT_PUSHPULL);
    palClearPad(GPIOC,13);
    chThdCreateStatic(waLED,sizeof(waLED),NORMALPRIO,thdLED,NULL);

    palSetPadMode(GPIOA, 9, PAL_MODE_STM32_ALTERNATE_PUSHPULL);
    palSetPadMode(GPIOA, 10, PAL_MODE_INPUT);
    sdStart(&SD1, NULL);

    shellInit();

    while (true) {
        if (!shelltp) shelltp = shellCreate(&sh_cfg, SHELL_WA_SIZE, NORMALPRIO);

        else if(chThdTerminatedX(shelltp)){
            chThdRelease(shelltp);
            shelltp = NULL;
        }

        chThdSleepMilliseconds(100);
    }

    return 0;
}
