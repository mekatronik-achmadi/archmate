ifneq ($(KERNELRELEASE),)
# kbuild part of makefile
obj-m  := pps-gmtimer.o

else
# normal makefile
KDIR = /lib/modules/$(shell uname -r)/build

.PHONY: default clean

default:
	$(MAKE) -C $(KDIR) M=$$PWD ARCH=arm

clean:
	$(MAKE) -C $(KDIR) M=$$PWD ARCH=arm clean

achmadi-00A0.dtbo: achmadi-00A0.dts
	dtc -@ -I dts -O dtb -o $@ $<
	
endif
