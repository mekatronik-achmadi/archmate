# target name
TARGET=appname

# compiler binary
CC=gcc
CXX=g++

# source directories
SRCDIR=./

# include directories
INCDIR=-I./

# build output directory
ODIR=build

# memory leak detection
# run binary with option:
#unset LD_PRELOAD
MEMLEAK=-fsanitize=address

# compiler options
COPT=-O0 -Wall -pthread
CFLAGS=$(COPT) $(MEMLEAK)
LFLAGS=$(COPT) $(MEMLEAK) -lm

################### Non Configurable ########################

CSRC=$(wildcard $(SRCDIR)/*.c)
CXXSRC=$(wildcard $(SRCDIR)/*.cpp)

COBJ=$(patsubst $(SRCDIR)/%.c,$(ODIR)/%.o,$(CSRC))
CXXOBJ=$(patsubst $(SRCDIR)/%.cpp,$(ODIR)/%.o,$(CXXSRC))

all: dir $(ODIR)/$(TARGET)

dir:
	mkdir -p $(ODIR)

$(ODIR)/$(TARGET): $(CXXOBJ) $(COBJ)
	$(CXX) $(CXXOBJ) $(COBJ) $(LFLAGS) -o $(ODIR)/$(TARGET)

$(ODIR)/%.o: $(SRCDIR)/%.cpp
	$(CXX) $(INCDIR) $(CFLAGS) -c $< -o $@

$(ODIR)/%.o: $(SRCDIR)/%.c
	$(CC) $(INCDIR) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(ODIR)/

.PHONY: all dir clean

