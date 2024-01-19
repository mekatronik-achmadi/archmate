// Package main provides ...
package main
import (
    "log"
    "os"

    "github.com/gotk3/gotk3/glib"
    "github.com/gotk3/gotk3/gtk"
)

const appID = "gotk3.glade.template"

func main() {
    app, err := gtk.ApplicationNew(appID,glib.APPLICATION_FLAGS_NONE)
    errorChk(err)

    app.Connect("activate", func() {
        builder,err := gtk.BuilderNewFromFile("main.glade")
        errorChk(err)

        obj,err := builder.GetObject("mWnd")
        wnd := toGtkWindow(obj)
        errorChk(err)

        signals := map[string]interface{}{
            "mBtnQuit_clicked_cb" : appQuit,
        }
        builder.ConnectSignals(signals)

        wnd.SetDefaultSize(200,100)
        wnd.Show()
        app.AddWindow(wnd)
    })

    os.Exit(app.Run(os.Args))
}

func appQuit() {
    gtk.MainQuit()
}



func toGtkWindow(obj glib.IObject)(*gtk.Window) {
    win := obj.(*gtk.Window)
    return win
}

func errorChk(e error) {
    if e != nil {
        log.Panic(e)
    }
}

