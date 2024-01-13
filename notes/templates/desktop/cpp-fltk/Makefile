# target name
TARGET=appname

# compiler binary
CC=g++

# source directories
SRCDIR=./

# include directories
INCDIR=-I./

# gui resource
GUIRC=gui.fl

# build output directory
ODIR=build

# compiler options
COPT=-O0 -Wall -pthread
CFLAGS=$(COPT) -I/usr/include/FL
LFLAGS=$(COPT) -lfltk -lfltk_forms

################### Non Configurable ########################

CSRC=$(wildcard $(SRCDIR)/*.cxx)
COBJ= $(patsubst $(SRCDIR)/%.cxx,$(ODIR)/%.o,$(CSRC))

all: dir uic $(ODIR)/$(TARGET)

dir:
	mkdir -p $(ODIR)

uic: $(GUIRC)
	fluid -c $(GUIRC)

$(ODIR)/$(TARGET): $(COBJ)
	$(CC) $(COBJ) $(LFLAGS) -o $(ODIR)/$(TARGET)

$(ODIR)/%.o: $(SRCDIR)/%.cxx
	$(CC) $(INCDIR) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(ODIR)/

.PHONY: all dir ui clean

