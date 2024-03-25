extern crate fltk;

use fltk::app;
use fltk::button::Button;
use fltk::dialog;
use fltk::prelude::*;
use fltk::window::Window;

fn main() {
    let app = app::App::default().with_scheme(app::Scheme::Gtk);

    let mut main_wnd = Window::new(100, 100, 200, 100, "FLTK Rust");
    let mut btn_msg = Button::new(0, 15, 200, 30, "Message");
    let mut btn_quit = Button::new(0, 55, 200, 30, "Quit");

    btn_msg.set_callback(move |_| {
        dialog::message_default("Rust FLTK Template");
    });

    btn_quit.set_callback(move |_| {
        app::quit();
    });

    main_wnd.end();
    main_wnd.show();

    app.run().unwrap();
}
