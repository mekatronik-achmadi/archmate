#include <gtk/gtk.h>

void mWnd_destroy_cb(){
    gtk_main_quit();
}

void mBtnQuit_clicked_cb(){
    gtk_main_quit();
}

void mBtnMsg_clicked_cb(){
    g_print("Template C GTK3\r\n");
}

int main(int argc, char *argv[])
{
    GtkBuilder *builder;
    GtkWidget *window;

    gtk_init(&argc, &argv);

    builder = gtk_builder_new_from_file("main.glade");

    window = GTK_WIDGET(gtk_builder_get_object(builder, "mWnd"));
    gtk_builder_connect_signals(builder, NULL);

    gtk_window_set_default_size(GTK_WINDOW(window), 200, 100);
    gtk_window_set_resizable (GTK_WINDOW(window), FALSE);

    g_object_unref(builder);

    gtk_widget_show(window);
    gtk_main();

    return 0;
}
