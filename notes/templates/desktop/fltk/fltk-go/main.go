package main

import (
    "fmt"
    "github.com/pwiecz/go-fltk"
)

func main() {
    wind := fltk.NewWindow(200,100)
    wind.SetLabel("Go FLTK Template")
    btnMsg := fltk.NewButton(0,30,200,30,"Message");
    btnQuit := fltk.NewButton(0,70,200,30,"Quit");

    btnMsg.SetCallback(func() {
        fltk.MessageBox("Info","FLTK GoLang Template")
    });

    btnQuit.SetCallback(func() {
        fmt.Println("Unimplemented for now")
    });

    wind.End()
    wind.Show()

    fltk.Run()
}

