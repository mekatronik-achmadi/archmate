#include "gui.h"

static void on_btnMsg(Fl_Widget* w, void* p){
    fl_message("Template FLTK C++");
}

static void on_btnQuit(Fl_Widget* w,void* p){
    ((Gui*)p)->close();
}

Gui::Gui() {
    mainWnd = new Fl_Window(170,70,"Template FLTK C++");
    btnMsg = new Fl_Button(0,10,170,25,"Message");
    btnQuit = new Fl_Button(0,40,170,25,"Quit");

    btnMsg->callback(on_btnMsg,NULL);
    btnQuit->callback(on_btnQuit,this);

    mainWnd->end();
}

void Gui::show(int argc,char* argv[]){
    mainWnd->show(argc,argv);
}

void Gui::close(){
    mainWnd->hide();
}


