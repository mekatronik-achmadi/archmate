#include <stdio.h>

#include "gfx.h"

static GListener gl;
static GHandle btnMsg;
static GHandle btnQuit;
static GHandle ghContainerPage;

static void buildWidgets(void){
    GWidgetInit wi;
    gwinWidgetClearInit(&wi);

    wi.g.show = TRUE;
    wi.g.width = 100;
    wi.g.height = 100;
    wi.g.x = 0;
    wi.g.y = 0;
    ghContainerPage = gwinContainerCreate(0, &wi, 0);

    wi.g.show = TRUE;
    wi.g.width = 100;
    wi.g.height = 50;
    wi.g.parent = ghContainerPage;
    wi.g.y = 10;
    wi.g.x = 20;
    wi.text = "Message";
    btnMsg = gwinButtonCreate(0, &wi);

    wi.g.show = TRUE;
    wi.g.width = 100;
    wi.g.height = 50;
    wi.g.parent = ghContainerPage;
    wi.g.y = 60;
    wi.g.x = 20;
    wi.text = "Quit";
    btnQuit = gwinButtonCreate(0, &wi);
}

int main(void) {
    GEvent *pe;

    gfxInit();

    gwinSetDefaultFont(gdispOpenFont("DejaVuSans12_aa"));
    gwinSetDefaultStyle(&WhiteWidgetStyle,FALSE);
    gdispClear(White);

    buildWidgets();

    geventListenerInit(&gl);
    gwinAttachListener(&gl);

    while(TRUE) {
        pe = geventEventWait(&gl, TIME_INFINITE);

        switch (pe->type) {
            case GEVENT_GWIN_BUTTON:
                if(((GEventGWinButton*)pe)->gwin==btnMsg) {
                    printf("Template C uGFX in SDL2\r\n");
                }

                else if(((GEventGWinButton*)pe)->gwin==btnQuit) {
                    printf("Exit unavailable in SDL2\r\n");
                }
                break;
            default:
                break;
        }
    }

    return 0;
}

