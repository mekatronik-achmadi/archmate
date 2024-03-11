#ifndef GUI_H
#define GUI_H

#include "wx/wxprec.h"
#ifndef WX_PRECOMP
  #include "wx/wx.h"
#endif

#include "wx/msgdlg.h"

#include "Ui_appGui.h"

class MainGUI : public frmMain
{
  public:
    MainGUI(const wxString &title);
    ~MainGUI();

    void btnMsg_clicked(wxCommandEvent& event);
    void btnQuit_clicked(wxCommandEvent& event);
};

#endif
