#include "gui.h"

MainGUI::MainGUI(const wxString &title)
    : frmMain(NULL, wxID_ANY, title,wxDefaultPosition,wxSize(200,150),wxDEFAULT_FRAME_STYLE & ~wxRESIZE_BORDER)
{}

MainGUI::~MainGUI()
{}

void MainGUI::on_btnMsg_clicked(wxCommandEvent& WXUNUSED(event)) {
    wxMessageBox( wxT("Template C++ wxGTK"),
    wxT("Template"),
    wxICON_INFORMATION);
}

void MainGUI::on_btnQuit_clicked(wxCommandEvent& WXUNUSED(event)){
    Close(true);
}
