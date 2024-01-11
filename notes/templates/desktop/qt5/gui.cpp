#include "gui.h"
#include "ui_gui.h"

Gui::Gui(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::Gui)
{
    ui->setupUi(this);
    setFixedSize(200,100);
}

Gui::~Gui()
{
    delete ui;
}


void Gui::on_btnQuit_clicked()
{
    QApplication::quit();
}


void Gui::on_btnMsg_clicked()
{
    QMessageBox::information(this,"Template","Template C++ Qt",QMessageBox::Ok);
}

