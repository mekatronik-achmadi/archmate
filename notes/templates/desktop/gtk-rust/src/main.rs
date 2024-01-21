extern crate gtk;
use gtk::prelude::*;
use std::path;

pub fn main() {
    let _ = gtk::init();

    let ui_file = path::Path::new("target/debug/main.glade");
    let builder  = gtk::Builder::from_file(ui_file);

    let m_wnd : gtk::Window = builder.object("mWnd").unwrap();
    let m_btn_quit : gtk::Button = builder.object("mBtnQuit").unwrap();
    let m_btn_msg : gtk::Button = builder.object("mBtnMsg").unwrap();

    m_btn_quit.connect_clicked(move |_| {
        gtk::main_quit();
    });

    m_btn_msg.connect_clicked(move |_| {
        let msg_box = gtk::MessageDialog::builder()
            .message_type(gtk::MessageType::Info)
            .buttons(gtk::ButtonsType::Ok)
            .text("Template GTK Rust")
            .build();

        msg_box.run();
        msg_box.hide();
    });

    m_wnd.set_default_size(200, 100);
    m_wnd.show_all();

    gtk::main();
}
