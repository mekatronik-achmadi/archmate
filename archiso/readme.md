# Custom ArchISO

This section contains scripts to build a simple Arch-Linux ISO.
To try, there are two options:
- [Download Examples](#download-example)
    + [CLI Variant](#cli-variant)
    + [MATE Variant](#mate-variant)
- [Build Yourself](#build-yourself)

Any my custom package recipes that build these ISO can be found [here](https://github.com/mekatronik-achmadi/archmate/tree/main/pkgbuilds/custom).

## Download Example

There are two variants: Command Line Interface and MATE Desktop.
You can download from [SourceForge]().

### CLI variant

This ArchISO using CLI BASH as default interface and Openbox as optional.

CLI ISO automatically login into a BASH interface after booting using **live** user.

![](screenshots/archcli.png)

Using [TMux](https://github.com/tmux/tmux/wiki), you can have multiple CLI BASH.

![](screenshots/archtmux.png)

Optionally, you can enter X11 Session with Openbox using command:

```sh
startx /usr/bin/openbox-session
```

![](screenshots/archob.png)

### MATE variant

This ArchISO provide MATE Desktop and Openbox with LightDM as login manager.

After booting, it will show the LightDM to choose session:

![](screenshots/archdm.png)

If MATE desktop chosen, it will login into Mate desktop using **live** user.

![](screenshots/archmate.png)

## Build Yourself