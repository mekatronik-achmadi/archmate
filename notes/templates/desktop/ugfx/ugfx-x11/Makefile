# Possible Targets:	all clean Debug cleanDebug Release cleanRelease

##############################################################################################
# Settings
#

# General settings
	# See $(GFXLIB)/tools/gmake_scripts/readme.txt for the list of variables
	OPT_OS					= linux
	OPT_LINK_OPTIMIZE		= yes
	# Change this next setting (or add the explicit compiler flags) if you are not compiling for x86 linux
	OPT_CPU					= x64

# uGFX settings
	# See $(GFXLIB)/tools/gmake_scripts/library_ugfx.mk for the list of variables
	GFXLIB					= /opt/ugfxlib/ugfx29
	GFXBOARD				= Linux-X
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
CFLAGS   = $(MEMLEAK)
CXXFLAGS =
ASFLAGS  =
LDFLAGS  = $(MEMLEAK)

SRC      =
OBJS     =
DEFS     =
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
