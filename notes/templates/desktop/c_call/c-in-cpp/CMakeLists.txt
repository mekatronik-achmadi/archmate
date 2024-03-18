cmake_minimum_required(VERSION 3.9)
project(WrapperC)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# MemLeak check
add_compile_options("-fsanitize=address")
add_link_options("-fsanitize=address")

add_executable(main main.cpp cli.cpp cli.h pwr.c pwr.h)

