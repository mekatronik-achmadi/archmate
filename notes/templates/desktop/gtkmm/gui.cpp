#include "gui.h"

Gui::Gui(BaseObjectType *cobject, const Glib::RefPtr<Gtk::Builder> &refGlade)
    : Gtk::Window(cobject), mBuilder(refGlade)
{
    set_default_size(200, 100);

    mBuilder->get_widget("mBtnMsg",mBtnMsg);
    mBuilder->get_widget("mBtnQuit",mBtnQuit);

    mBtnMsg->signal_clicked().connect(sigc::mem_fun(*this,&Gui::on_mBtnMsg));
    mBtnQuit->signal_clicked().connect(sigc::mem_fun(*this,&Gui::on_mBtnQuit));
}

Gui::~Gui(){

}

void Gui::on_mBtnMsg(){
    std::cout << "Template C++ GTK (GTKMM)\r\n";
}

void Gui::on_mBtnQuit(){
    std::cout << "Unimplemented\r\n";
}

