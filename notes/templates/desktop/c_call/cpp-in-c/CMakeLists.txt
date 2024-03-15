cmake_minimum_required(VERSION 3.9)
project(WrapperCPP)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_VERBOSE_MAKEFILE ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_executable(main main.c pwr.cpp pwr_wrap.cpp pwr_wrap.h)

