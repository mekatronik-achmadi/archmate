# Possible Targets:	all clean Debug cleanDebug Release cleanRelease

##############################################################################################
# Settings
#

# General settings
	# See $(GFXLIB)/tools/gmake_scripts/readme.txt for the list of variables
	OPT_OS					= linux
	OPT_LINK_OPTIMIZE		= yes
	# Change this next setting (or add the explicit compiler flags) if you are not compiling for x86 linux
	OPT_CPU					= x86

# uGFX settings
	# See $(GFXLIB)/tools/gmake_scripts/library_ugfx.mk for the list of variables
	GFXLIB					= /opt/ugfxlib
	GFXBOARD				= Linux-SDL
	GFXDEMO					=
	include ./template/template.mk

# Linux settings
	# See $(GFXLIB)/tools/gmake_scripts/os_linux.mk for the list of variables

# memory leak detection
# run binary with option:
#unset LD_PRELOAD
MEMLEAK=-fsanitize=address

##############################################################################################
# Set these for your project
#

ARCH     =
SRCFLAGS = -ggdb -O0
CFLAGS   = `pkgconf sdl2 --cflags` -m32 $(MEMLEAK)
CXXFLAGS = `pkgconf sdl2 --cflags` -m32 $(MEMLEAK)
ASFLAGS  =
LDFLAGS  = `pkgconf sdl2 --libs` -m32 $(MEMLEAK)

SRC      =
OBJS     =
DEFS     = -DPKG_CONFIG_PATH=/usr/lib32/pkgconfig
LIBS     =
INCPATH  =
LIBPATH  =

##############################################################################################
# These should be at the end
#

include $(GFXLIB)/tools/gmake_scripts/library_ugfx.mk
include $(GFXLIB)/tools/gmake_scripts/os_$(OPT_OS).mk
include $(GFXLIB)/tools/gmake_scripts/compiler_gcc.mk
# *** EOF ***
