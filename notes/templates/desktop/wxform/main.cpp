#include "main.h"
#include "Ui_appGui.h"

IMPLEMENT_APP(MainApp);

bool MainApp::OnInit(){
    if(!wxApp::CallOnInit()) return false;

    frmMain *frame = new frmMain();
    frame->Show(true);

    return true;
}


