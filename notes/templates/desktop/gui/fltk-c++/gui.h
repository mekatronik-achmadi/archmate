#ifndef GUI_H
#define GUI_H

#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Button.H>
#include <FL/fl_message.H>

class Gui
{
public:
    Gui ();

    Fl_Window *mainWnd;
    Fl_Button *btnMsg;
    Fl_Button *btnQuit;

    void show(int argc, char* argv[]);
    void close();
};

#endif
