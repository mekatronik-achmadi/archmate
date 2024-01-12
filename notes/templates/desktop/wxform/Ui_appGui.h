///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version 3.10.1)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#pragma once

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/stattext.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/button.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/sizer.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class frmMain
///////////////////////////////////////////////////////////////////////////////
class frmMain : public wxFrame
{
	private:

	protected:
		wxStaticText* txtTitle;
		wxButton* mBtnMsg;
		wxButton* mBtnQuit;

		// Virtual event handlers, override them in your derived class
		virtual void on_btnMsg_clicked( wxCommandEvent& event ) { event.Skip(); }
		virtual void on_btnQuit_clicked( wxCommandEvent& event ) { event.Skip(); }


	public:

		frmMain( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxEmptyString, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 250,150 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );

		~frmMain();

};

