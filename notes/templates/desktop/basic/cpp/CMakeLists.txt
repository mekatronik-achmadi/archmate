cmake_minimum_required(VERSION 3.9)
project(Basic)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# MemLeak check
add_compile_options("-fsanitize=address")
add_link_options("-fsanitize=address")

add_executable(appname main.cpp cli.cpp cli.h)
