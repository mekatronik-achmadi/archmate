# target name
TARGET=appname

# compiler binary
CC=g++
CFB=wxformbuilder

# source directories
SRCDIR=./

# include directories
INCDIR=-I./

# form file
FORM=appGui.fbp

# build output directory
ODIR=build

# compiler options
COPT=-O0 -Wall -pthread
CFLAGS=$(COPT) $(shell wx-config --cflags)
LFLAGS=$(COPT) $(shell wx-config --libs)


################### Non Configurable ########################

UISRC=$(wildcard $SRCDIR/Ui_*)
CSRC=$(wildcard $(SRCDIR)/*.cpp)
COBJ= $(patsubst $(SRCDIR)/%.cpp,$(ODIR)/%.o,$(CSRC))

all: dir ui $(ODIR)/$(TARGET)

dir:
	mkdir -p $(ODIR)

ui:
	$(CFB) -g -l c++ $(FORM)
	mv -vf $(UISRC) $(ODIR)/

$(ODIR)/$(TARGET): $(COBJ)
	$(CC) $(COBJ) $(LFLAGS) -o $(ODIR)/$(TARGET)

$(ODIR)/%.o: $(SRCDIR)/%.cpp
	$(CC) $(INCDIR) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(ODIR)/

.PHONY: all dir clean

