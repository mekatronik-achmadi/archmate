#ifndef GUI_H
#define GUI_H

#include <QObject>
#include <QMainWindow>
#include <QMessageBox>

QT_BEGIN_NAMESPACE
namespace Ui { class Gui; }
QT_END_NAMESPACE

class Gui : public QMainWindow
{
    Q_OBJECT

public:
    Gui(QWidget *parent = nullptr);
    ~Gui();

private slots:
    void btnQuit_clicked();
    void btnMsg_clicked();

private:
    Ui::Gui *ui;
};
#endif // GUI_H
