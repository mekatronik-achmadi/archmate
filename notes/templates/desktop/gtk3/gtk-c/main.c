#include <gtk/gtk.h>

void mWnd_destroy(){
    gtk_main_quit();
}

void mBtnQuit_clicked(){
    gtk_main_quit();
}

void mBtnMsg_clicked(){
    GtkWidget *msgbox;

    msgbox = gtk_message_dialog_new(NULL, 0, GTK_MESSAGE_INFO, GTK_BUTTONS_OK, "Template C GTK");
    gtk_dialog_run(GTK_DIALOG(msgbox));
    gtk_widget_destroy(GTK_WIDGET(msgbox));
}

int main(int argc, char *argv[])
{
    GtkBuilder *builder;
    GtkWindow *mWnd;
    GtkButton *mBtnMsg;
    GtkButton *mBtnQuit;

    gtk_init(&argc, &argv);

    builder = gtk_builder_new_from_file("main.glade");

    mWnd = GTK_WINDOW(gtk_builder_get_object(builder, "mWnd"));
    mBtnMsg = GTK_BUTTON(gtk_builder_get_object(builder, "mBtnMsg"));
    mBtnQuit = GTK_BUTTON(gtk_builder_get_object(builder, "mBtnQuit"));

    g_object_unref(builder);

    gtk_window_set_default_size(mWnd, 200, 100);
    gtk_window_set_resizable (mWnd, FALSE);
    g_signal_connect(G_OBJECT(mWnd), "destroy", G_CALLBACK(mWnd_destroy), NULL);

    g_signal_connect(G_OBJECT(mBtnMsg), "clicked", G_CALLBACK(mBtnMsg_clicked), NULL);
    g_signal_connect(G_OBJECT(mBtnQuit), "clicked", G_CALLBACK(mBtnQuit_clicked), NULL);

    gtk_widget_show(GTK_WIDGET(mWnd));
    gtk_main();

    return 0;
}
