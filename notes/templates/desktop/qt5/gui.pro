#mkdir -p build/
#cd build/
#qmake-qt5 ../
#bear -- make all
#cp -f compile_commands.json ../

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

SOURCES += \
    main.cpp \
    gui.cpp

HEADERS += \
    gui.h

FORMS += \
    gui.ui

