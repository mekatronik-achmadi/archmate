#include "gui.h"

class MainApp : public wxApp
{
public:
    virtual bool OnInit();
};

IMPLEMENT_APP(MainApp);

bool MainApp::OnInit(){
    if(!wxApp::OnInit()) return false;

    MainGUI *frame = new MainGUI(wxT("Template"));
    frame->Show(true);

    return true;
}

