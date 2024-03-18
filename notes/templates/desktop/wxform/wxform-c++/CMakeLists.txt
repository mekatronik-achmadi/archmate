cmake_minimum_required(VERSION 3.9)
project(Basic)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# MemLeak check
add_compile_options("-fsanitize=address")
add_link_options("-fsanitize=address")

find_package(wxWidgets REQUIRED)

include(${wxWidgets_USE_FILE})
add_library(Gui Ui_appGui.cpp Ui_appGui.h)

add_executable(appname main.cpp gui.cpp gui.h)
add_dependencies(appname Gui)
target_link_libraries(appname Gui)
target_link_libraries(appname ${wxWidgets_LIBRARIES})

