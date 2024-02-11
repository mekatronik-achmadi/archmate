#include "gui.h"
#include "ui_gui.h"

Gui::Gui(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::Gui)
{
    ui->setupUi(this);
    setFixedSize(200,100);

    connect(ui->btnQuit,SIGNAL(clicked()),this,SLOT(btnQuit_clicked()));
    connect(ui->btnMsg,SIGNAL(clicked()),this,SLOT(btnMsg_clicked()));
}

Gui::~Gui()
{
    delete ui;
}


void Gui::btnQuit_clicked()
{
    QApplication::quit();
}


void Gui::btnMsg_clicked()
{
    QMessageBox::information(this,"Template","Template C++ Qt",QMessageBox::Ok);
}

