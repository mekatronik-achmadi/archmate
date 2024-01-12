#ifndef MAIN_H
#define MAIN_H

#include "wx/wxprec.h"
#ifndef WX_PRECOMP
  #include "wx/wx.h"
#endif

class MainApp : public wxApp
{
private:

public:
    virtual bool OnInit();
};

#endif /* MAIN_H */
