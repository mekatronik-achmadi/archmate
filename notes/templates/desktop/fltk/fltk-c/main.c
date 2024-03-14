#include <cfltk/cfl.h>
#include <cfltk/cfl_window.h>

int main(int argc, char *argv[])
{
    Fl_Window *wind = Fl_Window_new_(100,100,200,100,"C FLTK Template");

    Fl_Window_end(wind);
    Fl_Window_show(wind);

    return Fl_run();
}
