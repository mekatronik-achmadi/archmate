# target name
TARGET=appname

# compiler binary
CC=g++

# source directories
SRCDIR=./

# include directories
INCDIR=-I./

# gui resource
GUIRC=gui.glade

# build output directory
ODIR=build

# memory leak detection
# run binary with option:
#unset LD_PRELOAD
MEMLEAK=-fsanitize=address

# compiler options
COPT=-O0 -Wall -pthread -rdynamic
CFLAGS=$(COPT) $(MEMLEAK) $(shell pkg-config --cflags gtkmm-3.0)
LFLAGS=$(COPT) $(MEMLEAK) $(shell pkg-config --libs gtkmm-3.0)


################### Non Configurable ########################

CSRC=$(wildcard $(SRCDIR)/*.cpp)
COBJ=$(patsubst $(SRCDIR)/%.cpp,$(ODIR)/%.o,$(CSRC))

all: dir $(ODIR)/$(TARGET)

dir:
	mkdir -p $(ODIR)

$(ODIR)/$(TARGET): $(COBJ)
	$(CC) $(COBJ) $(LFLAGS) -o $(ODIR)/$(TARGET)
	cp -vf $(GUIRC) $(ODIR)/$(GUIRC)

$(ODIR)/%.o: $(SRCDIR)/%.cpp
	$(CC) $(INCDIR) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(ODIR)/

.PHONY: all dir clean

