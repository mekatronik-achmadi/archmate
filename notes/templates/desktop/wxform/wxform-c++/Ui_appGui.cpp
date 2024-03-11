///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version 3.10.1)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "Ui_appGui.h"

///////////////////////////////////////////////////////////////////////////

frmMain::frmMain( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );

	wxBoxSizer* bMain;
	bMain = new wxBoxSizer( wxVERTICAL );

	txtTitle = new wxStaticText( this, wxID_ANY, wxT("Template WxWidget"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL );
	txtTitle->Wrap( -1 );
	bMain->Add( txtTitle, 1, wxALL|wxEXPAND, 5 );

	mBtnMsg = new wxButton( this, wxID_ANY, wxT("Message"), wxDefaultPosition, wxDefaultSize, 0 );
	bMain->Add( mBtnMsg, 1, wxALL|wxEXPAND, 5 );

	mBtnQuit = new wxButton( this, wxID_ANY, wxT("Quit"), wxDefaultPosition, wxDefaultSize, 0 );
	bMain->Add( mBtnQuit, 1, wxALL|wxEXPAND, 5 );


	this->SetSizer( bMain );
	this->Layout();

	this->Centre( wxBOTH );
}

frmMain::~frmMain()
{
}
