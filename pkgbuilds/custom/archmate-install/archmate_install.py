#!/usr/bin/python
# -*- coding: utf-8 -*-

"""@package ArchMateInstall
Arch Mate Install script.

Deploy Live ArchISO to a system.

Notes:
subprocess.Popen -> Logging, Not Waiting, Output Ignored, Continue when Fail
subprocess.run -> No Log, Waiting, Output Processed, Stop when Fail
"""

import wx
import os
import sys
import subprocess
from os import path
from wx import html as hl

import archmate_gui

class HtmlViewer(wx.Frame):
    def __init__(self, parent, filepath):
        wx.Frame.__init__(
            self,
            parent,
            -1,
            "HTML Viewer",
            size = (600, 600)
        )

        html = hl.HtmlWindow(self)
        self.Maximize(False)

        #if "gtk2" in wx.PlatformInfo:
        #    html.SetStandardFonts()

        html.LoadPage(filepath)

class ArchMateInstall(archmate_gui.frmArchInstall):
    """ArchMateInstall class

    Main class to run first
    """

    def __init__(self,parent):
        """Initialization function.

        Initiate text variables and status flags
        """

        archmate_gui.frmArchInstall.__init__(self,parent)

        self.m_txtHome.Disable()
        self.m_chkRoot.Disable()
        self.m_chkEFI.Disable()
        self.m_chkGRUB.Disable()

        self.msgConfirm = ""
        self.Host = ""
        self.User = ""
        self.Root = ""
        self.Home = ""
        self.UseHome = False
        self.EFI = ""
        self.UseEFI = False
        self.GRUB = ""
        self.Sfs = "/run/archiso/airootfs/"
        self.Squash = "/run/archiso/bootmnt/arch/x86_64/airootfs.sfs"
        self.UseUnsfs = True

        self.pid = None

        self.m_chkGRUB.SetValue(True)
        if path.exists("/sys/firmware/efi"):
            self.m_chkEFI.SetValue(True)
            self.m_txtEFI.Enable()
        else:
            self.m_chkEFI.SetValue(False)
            self.m_txtEFI.Disable()

        self.m_chkSfs.SetValue(False)
        self.m_chkUnsfs.SetValue(True)

    def OnBtnParted(self,event):
        """Command to start GParted program
        """

        if not path.exists("/usr/bin/gparted"):
            wx.MessageBox("No GParted program","Error", wx.OK|wx.ICON_ERROR)
            return

        subprocess.Popen('/usr/bin/gparted')

    def OnChkHome(self,event):
        if self.m_chkHome.IsChecked():
            self.m_txtHome.Enable()
        else:
            self.m_txtHome.Disable()

    def OnChkSfs(self,event):
        if self.m_chkSfs.IsChecked():
            self.m_chkUnsfs.SetValue(False)
        else:
            self.m_chkUnsfs.SetValue(True)

    def OnChkUnsfs(self,event):
        if self.m_chkUnsfs.IsChecked():
            self.m_chkSfs.SetValue(False)
        else:
            self.m_chkSfs.SetValue(True)

    def OnBtnHelp(self,event):
        htmlView = HtmlViewer(None, "/usr/share/archmate-install/help.html")
        htmlView.Show()

    def OnBtnInstall(self,event):
        """Command to start install processing
        """

        msgInfo = self.InstallInfo()
        if msgInfo:
            installConfirm = wx.MessageBox(self.msgConfirm,"Confirm ?",wx.OK|wx.CANCEL|wx.ICON_QUESTION)
            if installConfirm == wx.OK:
                self.m_btnParted.Disable()
                self.m_btnInstall.Disable()

                self.m_txtHost.Disable()
                self.m_txtUser.Disable()

                self.m_chkRoot.Disable()
                self.m_txtRoot.Disable()

                self.m_chkHome.Disable()
                self.m_txtHome.Disable()

                self.m_chkEFI.Disable()
                self.m_txtEFI.Disable()

                self.m_chkGRUB.Disable()
                self.m_txtGRUB.Disable()

                self.m_chkSfs.Disable()
                self.m_chkUnsfs.Disable()

                self.InstallProc()

    def CheckSameDisk(self):
        """Check if Partition and GRUB on same disk
        """

        if not self.GRUB == self.Root[0:len(self.GRUB)]:
            wx.MessageBox("Root not in same GRUB disk","Error", wx.OK|wx.ICON_ERROR)
            return False

        if self.m_chkHome.IsChecked():
            if not self.GRUB == self.Home[0:len(self.GRUB)]:
                wx.MessageBox("Home not same GRUB disk","Error", wx.OK|wx.ICON_ERROR)
                return False

        if self.m_chkEFI.IsChecked():
            if not self.GRUB == self.EFI[0:len(self.GRUB)]:
                wx.MessageBox("EFI not same GRUB disk","Error", wx.OK|wx.ICON_ERROR)
                return False

        if self.GRUB==self.Root or self.GRUB==self.Home or self.GRUB==self.EFI:
            wx.MessageBox("GRUB entry is same with something else","Error",wx.OK|wx.ICON_ERROR)
            return False

        if self.Root==self.Home or self.Root==self.EFI:
            wx.MessageBox("Root entry is same with something else","Error",wx.OK|wx.ICON_ERROR)
            return False

        if self.m_chkHome.IsChecked():
            if self.Home==self.EFI:
                wx.MessageBox("Home entry is same with something else","Error",wx.OK|wx.ICON_ERROR)
                return False

        return True

    def CheckPartFS(self):
        """Check if Partition not in intended format
        """
        r = subprocess.run(["blkid", "-s", "TYPE", "-o", "value",self.Root], stdout=subprocess.PIPE, stderr=None)
        typeFsRoot = r.stdout.decode('utf-8').rstrip()
        if not typeFsRoot=="ext4":
            wx.MessageBox("Root not in ext4 format","Error",wx.OK|wx.ICON_ERROR)
            return False

        if self.m_chkHome.IsChecked():
            r = subprocess.run(["blkid", "-s", "TYPE", "-o", "value",self.Home], stdout=subprocess.PIPE, stderr=None)
            typeFsHome = r.stdout.decode('utf-8').rstrip()
            if not typeFsHome=="ext4":
                wx.MessageBox("Home not in ext4 format","Error",wx.OK|wx.ICON_ERROR)
                return False

        if self.m_chkEFI.IsChecked():
            r = subprocess.run(["blkid", "-s", "TYPE", "-o", "value",self.EFI], stdout=subprocess.PIPE, stderr=None)
            typeFsEFI = r.stdout.decode('utf-8').rstrip()
            if not typeFsEFI=="vfat":
                wx.MessageBox("EFI not in vfat (fat32) format","Error",wx.OK|wx.ICON_ERROR)
                return False

        return True

    def CheckPartSize(self):
        """Check if Partition not in minimum size
        """

        r = subprocess.run(["fdisk", "-s", "--bytes", self.Root], stdout=subprocess.PIPE, stderr=None)
        sizeFsRoot = int(r.stdout.decode('utf-8').rstrip())/1000
        if sizeFsRoot < 12000:
            wx.MessageBox("Root size less than 12GB","Error",wx.OK|wx.ICON_ERROR)
            return False

        if self.m_chkEFI.IsChecked():
            r = subprocess.run(["fdisk", "-s", "--bytes", self.EFI], stdout=subprocess.PIPE, stderr=None)
            sizeFsEFI = int(r.stdout.decode('utf-8').rstrip())/1000
            if sizeFsEFI < 100:
                wx.MessageBox("EFI size less than 100MB","Error",wx.OK|wx.ICON_ERROR)
                return False

        return True

    def InstallInfo(self):
        """Gathering install informations
        """

        self.msgConfirm = ""

        self.Host = self.m_txtHost.GetValue()
        self.msgConfirm += "Hostname: " + self.Host + "\n"
        if not self.Host:
            wx.MessageBox("Hostname is empty","Error", wx.OK|wx.ICON_ERROR)
            return False

        self.User = self.m_txtUser.GetValue()
        self.msgConfirm += "Username: " + self.User + "\n"
        if not self.User:
            wx.MessageBox("Username is empty","Error", wx.OK|wx.ICON_ERROR)
            return False

        self.Root = self.m_txtRoot.GetValue()
        self.msgConfirm += "Root dev: " + self.Root + "\n"
        if not self.Root:
            wx.MessageBox("Root Address is empty","Error", wx.OK|wx.ICON_ERROR)
            return False

        if not path.exists(self.Root):
            wx.MessageBox("Root Address is not exist","Error", wx.OK|wx.ICON_ERROR)
            return False

        if self.m_chkHome.IsChecked():
            self.Home = self.m_txtHome.GetValue()
            self.msgConfirm += "Home dev: " + self.Home + "\n"
            if self.Home:
                self.UseHome = True
            else:
                wx.MessageBox("Home Address is empty","Error", wx.OK|wx.ICON_ERROR)
                return False

            if not path.exists(self.Home):
                wx.MessageBox("Home Address is not exist","Error", wx.OK|wx.ICON_ERROR)
                self.UseHome = False
                return False

        if self.m_chkEFI.IsChecked():
            self.EFI = self.m_txtEFI.GetValue()
            self.msgConfirm += "EFI dev: " + self.EFI + "\n"

            if not path.exists("/sys/firmware/efi"):
                wx.MessageBox("System NOT in EFI mode","Error", wx.OK|wx.ICON_ERROR)
                self.UseEFI = False
                return False

            if not self.EFI:
                wx.MessageBox("EFI Address is empty","Error", wx.OK|wx.ICON_ERROR)
                return False

            self.UseEFI = True

        if self.m_chkGRUB.IsChecked():
            self.GRUB = self.m_txtGRUB.GetValue()
            self.msgConfirm += "GRUB dev: " + self.GRUB + "\n"

            if not self.GRUB:
                wx.MessageBox("GRUB is empty","Error", wx.OK|wx.ICON_ERROR)
                return False

            if not path.exists(self.GRUB):
                wx.MessageBox("GRUB Address is not exist","Error", wx.OK|wx.ICON_ERROR)
                return False

        if path.exists("/sys/firmware/efi"):
            if not self.UseEFI:
                wx.MessageBox("System in EFI mode but not configured","Error", wx.OK|wx.ICON_ERROR)
                return False

        allSameDisk = self.CheckSameDisk()
        if not allSameDisk:
            return False

        correctFsType = self.CheckPartFS()
        if not correctFsType:
            return False

        correctFsSize = self.CheckPartSize()
        if not correctFsSize:
            return False

        if self.m_chkUnsfs.IsChecked():
            self.UseUnsfs = True
            self.msgConfirm += "Method: Unsquashfs" + "\n"
            self.msgConfirm += "Squashfs Path: " + self.Squash + "\n"
        else:
            self.UseUnsfs = False
            self.msgConfirm += "Method: Rsync" + "\n"
            self.msgConfirm += "Airootsfs Path: " + self.Sfs + "\n"

        return True

    def ConsoleLog(self,procID):
        """Console Message function
        """

        wx.GetApp().Yield()
        self.pid = procID.pid
        while procID.poll() is None:
            x = procID.stdout.readline().decode()
            self.m_txtConsole.write(x)
            wx.GetApp().Yield()

    def InstallProc(self):
        """Main Install process
        """

        stepMsg = "Mount target Root"
        self.m_lblLog.SetLabel(stepMsg)

        p = subprocess.Popen(["mkdir", "-p", "/target/"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        self.ConsoleLog(p)

        p = subprocess.Popen(["mount", "-v", "-o", "rw",self.Root,"/target/"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        self.ConsoleLog(p)

        stepMsg = "Filling-up filesystem"
        self.m_lblLog.SetLabel(stepMsg)

        if self.UseUnsfs:
            self.m_txtConsole.write("Unsquashfs started. This program freeze for a while\n")
            p = subprocess.Popen(["unsquashfs", "-q", "-f", "-d", "/target/", self.Squash], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
            self.ConsoleLog(p)
        else:
            self.m_txtConsole.write("RSync started. This process take a while\n")
            p = subprocess.Popen(["rsync", "-q", "-avh", self.Sfs, "/target/"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
            self.ConsoleLog(p)

        self.m_txtConsole.write("Filling-up Completed\n\n")

        stepMsg = "Regenerating locale"
        self.m_lblLog.SetLabel(stepMsg)

        p = subprocess.Popen(["arch-chroot", "/target", "locale-gen"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        self.ConsoleLog(p)

        self.m_txtConsole.write("Locale Completed\n\n")

        stepMsg = "Rebuild Initramfs"
        self.m_lblLog.SetLabel(stepMsg)

        preset  = 'ALL_config="/etc/mkinitcpio.conf"\n'
        preset += 'ALL_kver="/boot/vmlinuz-linux"\n'
        preset += "PRESETS=('default')\n"
        preset += 'default_image="/boot/initramfs-linux.img"\n'
        presetFile = open("/target/etc/mkinitcpio.d/archlinux.preset","w")
        presetFile.write(preset)
        presetFile.close()

        sed_args  = 's@'
        sed_args += 'base udev modconf memdisk archiso archiso_loop_mnt consolefont kms block filesystems keyboard'
        sed_args += '@'
        sed_args += 'base udev autodetect modconf memdisk consolefont kms block filesystems keyboard fsck'
        sed_args += '@g'
        p = subprocess.Popen(["sed", "-i", sed_args, "/target/etc/mkinitcpio.conf"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        self.ConsoleLog(p)

        r = subprocess.run(["arch-chroot", "/target", "uname", "-r"], stdout=subprocess.PIPE, stderr=None)
        kernelver = r.stdout.decode('utf-8').rstrip()
        vmlinuz = "/target/usr/lib/modules/" + kernelver + "/vmlinuz"

        self.m_txtConsole.write("Using kernel:\n")
        self.m_txtConsole.write(vmlinuz)
        self.m_txtConsole.write("\n")

        p = subprocess.Popen(["cp", "-f", vmlinuz , "/target/boot/vmlinuz-linux"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        self.ConsoleLog(p)

        p = subprocess.Popen(["arch-chroot", "/target", "mkinitcpio", "-p", "archlinux"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        self.ConsoleLog(p)

        self.m_txtConsole.write("Initramfs Completed\n\n")

        stepMsg = "Configure Fstab"
        self.m_lblLog.SetLabel(stepMsg)

        r = subprocess.run(["blkid", "-s", "UUID", "-o", "value",self.Root], stdout=subprocess.PIPE, stderr=None)
        self.RootUuid = r.stdout.decode('utf-8')
        self.m_txtConsole.write("Root UUID: "+self.RootUuid)

        r = subprocess.run(["blkid", "-s", "TYPE", "-o", "value",self.Root], stdout=subprocess.PIPE, stderr=None)
        self.RootType = r.stdout.decode('utf-8')
        self.m_txtConsole.write("Root Type: "+self.RootType)

        strFstabRoot = "UUID=%s / %s defaults 0 1\n" % (self.RootUuid.rstrip(),self.RootType.rstrip())
        fstabFile = open("/target/etc/fstab","w")
        fstabFile.write(strFstabRoot)
        fstabFile.close()

        if self.UseHome:
            r = subprocess.run(["blkid", "-s", "UUID", "-o", "value",self.Home], stdout=subprocess.PIPE, stderr=None)
            self.HomeUuid = r.stdout.decode('utf-8')
            self.m_txtConsole.write("Home UUID: "+self.HomeUuid)

            r = subprocess.run(["blkid", "-s", "TYPE", "-o", "value",self.Home], stdout=subprocess.PIPE, stderr=None)
            self.HomeType = r.stdout.decode('utf-8')
            self.m_txtConsole.write("Home Type: "+self.HomeType)

            strFstabHome = "UUID=%s /home %s defaults 0 2\n" % (self.HomeUuid.rstrip(),self.HomeType.rstrip())
            fstabFile = open("/target/etc/fstab","a")
            fstabFile.write(strFstabHome)
            fstabFile.close()

        self.m_txtConsole.write("Fstab Completed\n\n")

        stepMsg = "Configure Hostname"
        self.m_lblLog.SetLabel(stepMsg)

        hostFile = open("/target/etc/hostname","w")
        hostFile.write(self.Host)
        hostFile.close()

        stepMsg = "Configure UserConfig"
        self.m_lblLog.SetLabel(stepMsg)

        self.m_txtConsole.write("Remove live user\n")
        p = subprocess.Popen(["arch-chroot", "/target", "userdel", "-rf", "live"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        self.ConsoleLog(p)

        if self.UseHome:
            p = subprocess.Popen(["mount", "-v", "-o", "rw",self.Home,"/target/home"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
            self.ConsoleLog(p)

        self.m_txtConsole.write("Create installed user\n")
        p = subprocess.Popen(["arch-chroot","/target","useradd","-m","-g","users","-G","wheel,storage,power,video,tty","-s","/bin/bash","-c",self.User,self.User], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        self.ConsoleLog(p)

        p = subprocess.Popen(["arch-chroot","/target","sudo","-u",self.User,"mkdir","-p","/home/"+self.User+"/"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        self.ConsoleLog(p)

        p = subprocess.Popen(["arch-chroot","/target","sudo","-u",self.User,"rsync","-a","/etc/skel/","/home/"+self.User+"/"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        self.ConsoleLog(p)

        p = subprocess.Popen(["arch-chroot","/target","passwd","-d","root"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        self.ConsoleLog(p)

        p = subprocess.Popen(["arch-chroot","/target","passwd","-d",self.User], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        self.ConsoleLog(p)

        p = subprocess.Popen(["arch-chroot","/target","groupadd","-f","-r","autologin"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        self.ConsoleLog(p)

        p = subprocess.Popen(["arch-chroot","/target","gpasswd","-a", self.User, "autologin"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        self.ConsoleLog(p)

        sed_login = 's@'
        sed_login += 'live'
        sed_login += '@'
        sed_login += self.User
        sed_login += '@g'

        p = subprocess.Popen(["sed", "-i", sed_login, "/target/etc/lightdm/lightdm.conf"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        self.ConsoleLog(p)

        p = subprocess.Popen(["sed", "-i", sed_login, "/target/etc/systemd/system/getty@tty1.service.d/autologin.conf"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        self.ConsoleLog(p)

        if self.UseHome:
            p = subprocess.Popen(["umount","-v","/target/home"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
            self.ConsoleLog(p)

        self.m_txtConsole.write("UserConfig Completed\n\n")

        stepMsg = "Configure GRUB Bootloader"
        self.m_lblLog.SetLabel(stepMsg)

        if self.UseEFI:
            uefiNum = "".join(self.EFI.rsplit(self.GRUB))
            p = subprocess.Popen(["arch-chroot", "/target", "parted", self.GRUB, "set", uefiNum, "esp", "on"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
            self.ConsoleLog(p)

            p = subprocess.Popen(["arch-chroot", "/target", "parted", self.GRUB, "set", uefiNum, "boot", "on"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
            self.ConsoleLog(p)

            p = subprocess.Popen(["mkdir", "-p", "/target/boot/EFI"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
            self.ConsoleLog(p)

            p = subprocess.Popen(["mount", "-v", "-o", "rw", self.EFI, "/target/boot/EFI"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
            self.ConsoleLog(p)

            #p = subprocess.Popen(["arch-chroot", "/target", "grub-install", "--recheck", "--removable", "--target=x86_64-efi", "--efi-directory=/boot/EFI/", "--bootloader-id=grub_uefi"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
            p = subprocess.Popen(["arch-chroot", "/target", "grub-install", "--recheck", "--target=x86_64-efi", "--efi-directory=/boot/EFI/", "--bootloader-id=grub_uefi"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
            self.ConsoleLog(p)

            p = subprocess.Popen(["arch-chroot", "/target", "grub-mkconfig", "-o", "/boot/grub/grub.cfg"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
            self.ConsoleLog(p)

            p = subprocess.Popen(["umount","-v","/target/boot/EFI"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
            self.ConsoleLog(p)

            r = subprocess.run(["blkid", "-s", "UUID", "-o", "value",self.EFI], stdout=subprocess.PIPE, stderr=None)
            self.EfiUuid = r.stdout.decode('utf-8')
            self.m_txtConsole.write("EFI UUID: "+self.EfiUuid)

            r = subprocess.run(["blkid", "-s", "TYPE", "-o", "value",self.EFI], stdout=subprocess.PIPE, stderr=None)
            self.EfiType = r.stdout.decode('utf-8')
            self.m_txtConsole.write("EFI Type: "+self.EfiType)

            strFstabEfi = "UUID=%s /boot/EFI %s defaults 0 3\n" % (self.EfiUuid.rstrip(),self.EfiType.rstrip())
            fstabFile = open("/target/etc/fstab","a")
            fstabFile.write(strFstabEfi)
            fstabFile.close()

        else:
            rootNum = "".join(self.Root.rsplit(self.GRUB))
            p = subprocess.Popen(["arch-chroot", "/target", "parted", self.GRUB, "set", rootNum, "boot", "on"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
            self.ConsoleLog(p)

            p = subprocess.Popen(["arch-chroot", "/target", "grub-install", "--recheck", "--target=i386-pc",self.GRUB], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
            self.ConsoleLog(p)

            p = subprocess.Popen(["arch-chroot", "/target", "grub-mkconfig", "-o", "/boot/grub/grub.cfg"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
            self.ConsoleLog(p)

        self.m_txtConsole.write("Bootloader Completed\n\n")

        stepMsg = "Remove Installer script"
        self.m_lblLog.SetLabel(stepMsg)

        p = subprocess.Popen(["arch-chroot", "/target", "pacman", "-Rns", "--noconfirm", "archmate-install"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        self.ConsoleLog(p)

        stepMsg = "Unmount target Root"
        self.m_lblLog.SetLabel(stepMsg)

        p = subprocess.Popen(["umount","-v","/target/"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        self.ConsoleLog(p)

        self.m_lblLog.SetLabel("Install Completed")

        self.m_txtConsole.write("\nInstallation Finsished\n")
        self.m_txtConsole.write("You can reboot manually")


if not os.geteuid()==0:
    sys.exit('This script must be run as root!')

app = wx.App(False)
frame = ArchMateInstall(None)
frame.Show(True)
app.MainLoop()
