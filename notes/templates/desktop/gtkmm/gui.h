#ifndef GUI_H
#define GUI_H

#include <iostream>
#include <gtkmm-3.0/gtkmm.h>

class Gui : public Gtk::Window
{
private:


public:
    Gui(BaseObjectType *cobject, const Glib::RefPtr<Gtk::Builder> &refGlade);
    virtual ~Gui();

protected:
    Glib::RefPtr<Gtk::Builder> mBuilder;
    Glib::RefPtr<Gtk::Application> mApp;

    Gtk::Button *mBtnMsg;
    Gtk::Button *mBtnQuit;

    void on_mBtnMsg(void);
    void on_mBtnQuit(void);
};

#endif /* GUI_H */
