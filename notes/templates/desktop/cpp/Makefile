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
CFLAGS=$(COPT)
LFLAGS=$(COPT)

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
	rm -rf $(ODIR)/

.PHONY: all dir clean

