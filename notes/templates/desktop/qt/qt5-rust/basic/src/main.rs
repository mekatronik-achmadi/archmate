use cxx_qt_lib::QGuiApplication;

fn main() {
    let mut app = QGuiApplication::new();

    if let Some(app) = app.as_mut() {
        app.exec();
    }
}

