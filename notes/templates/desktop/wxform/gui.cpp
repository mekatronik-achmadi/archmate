#include "gui.h"

MainGUI::MainGUI(const wxString &title)
    : frmMain(NULL, wxID_ANY, title,wxDefaultPosition,wxSize(200,150),wxDEFAULT_FRAME_STYLE & ~wxRESIZE_BORDER)
{
    mBtnMsg->Connect(wxEVT_COMMAND_BUTTON_CLICKED,wxCommandEventHandler(MainGUI::btnMsg_clicked),NULL,this);
    mBtnQuit->Connect(wxEVT_COMMAND_BUTTON_CLICKED,wxCommandEventHandler(MainGUI::btnQuit_clicked),NULL,this);
}

MainGUI::~MainGUI()
{}

void MainGUI::btnMsg_clicked(wxCommandEvent& WXUNUSED(event)) {
    wxMessageBox( wxT("Template C++ wxGTK"),
    wxT("Template"),
    wxICON_INFORMATION);
}

void MainGUI::btnQuit_clicked(wxCommandEvent& WXUNUSED(event)){
    Close(true);
}
