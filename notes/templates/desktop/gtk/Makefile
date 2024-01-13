# target name
TARGET=appname

# compiler binary
CC=gcc

# source directories
SRCDIR=./

# include directories
INCDIR=-I./

# gui resource
GUIRC=main.glade

# build output directory
ODIR=build

# compiler options
COPT=-O0 -Wall -pthread -rdynamic
CFLAGS=$(COPT) $(shell pkg-config --cflags gtk+-3.0)
LFLAGS=$(COPT) $(shell pkg-config --libs gtk+-3.0)


################### Non Configurable ########################

CSRC=$(wildcard $(SRCDIR)/*.c)
COBJ= $(patsubst $(SRCDIR)/%.c,$(ODIR)/%.o,$(CSRC))

all: dir $(ODIR)/$(TARGET)

dir:
	mkdir -p $(ODIR)

$(ODIR)/$(TARGET): $(COBJ)
	$(CC) $(COBJ) $(LFLAGS) -o $(ODIR)/$(TARGET)
	cp -vf $(GUIRC) $(ODIR)/$(GUIRC)

$(ODIR)/%.o: $(SRCDIR)/%.c
	$(CC) $(INCDIR) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(ODIR)/

.PHONY: all dir clean

