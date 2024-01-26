# target name
TARGET=appname

# compiler binary
CC=g++

# source directories
SRCDIR=./

# include directories
INCDIR=-I./

# build output directory
ODIR=build

# compiler options
COPT=-O0 -Wall -pthread
CFLAGS=$(COPT) $(shell wx-config --cflags)
LFLAGS=$(COPT) $(shell wx-config --libs)


################### Non Configurable ########################

CSRC=$(wildcard $(SRCDIR)/*.cpp)
COBJ=$(patsubst $(SRCDIR)/%.cpp,$(ODIR)/%.o,$(CSRC))

all: dir $(ODIR)/$(TARGET)

dir:
	mkdir -p $(ODIR)

$(ODIR)/$(TARGET): $(COBJ)
	$(CC) $(COBJ) $(LFLAGS) -o $(ODIR)/$(TARGET)

$(ODIR)/%.o: $(SRCDIR)/%.cpp
	$(CC) $(INCDIR) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(UISRC) $(ODIR)/

.PHONY: all dir clean

