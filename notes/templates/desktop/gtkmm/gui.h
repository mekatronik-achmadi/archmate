#ifndef GUI_H
#define GUI_H

#include <gtkmm-3.0/gtkmm.h>

class Gui : public Gtk::Window
{
private:


public:
    Gui(BaseObjectType *cobject, const Glib::RefPtr<Gtk::Builder> &refGlade);
    virtual ~Gui();

protected:
    Glib::RefPtr<Gtk::Builder> mBuilder;

    Gtk::Button *mBtnMsg;
    Gtk::Button *mBtnQuit;
    Gtk::Window *mWnd;

    void on_mBtnMsg(void);
    void on_mBtnQuit(void);
};

#endif /* GUI_H */
