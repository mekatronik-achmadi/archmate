#include "gui.h"

int main(int argc, char *argv[])
{
    auto app = Gtk::Application::create(argc,argv,"");

    Glib::RefPtr<Gtk::Builder> builder = Gtk::Builder::create()->create_from_file("gui.glade");
    Gui *wnd = 0;
    builder->get_widget_derived("mWnd",wnd);

    return app->run(*wnd);
}
