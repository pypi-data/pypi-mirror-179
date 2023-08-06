#pragma once

#include "class_context.hpp"

#include "../full_console.hpp"
#include "../machine.hpp"
#include "../vec2.hpp"

#include <pybind11/detail/common.h>
#include <pybind11/pybind11.h>

#include <filesystem>
#include <memory>
#include <string>
#include <tuple>

namespace py = pybind11;
namespace fs = std::filesystem;

inline std::shared_ptr<FullConsole> make_console(int32_t cols, int32_t rows,
                                                 std::string const& font_file,
                                                 Vec2f const& tile_size,
                                                 int font_size)
{
    fs::path p{font_file};

    auto ts = std::pair<int, int>{tile_size.x, tile_size.y};
    auto font = font_file.empty()
                    ? std::make_shared<ConsoleFont>(FreetypeFont::unscii, ts)
                    : std::make_shared<ConsoleFont>(p.string(), font_size, ts);

    auto con = std::make_shared<PixConsole>(cols, rows, font);
    auto fcon = std::make_shared<FullConsole>(con, Machine::get_instance().sys);

    return fcon;
}

inline void add_console_class(py::module_ const& mod)
{
    // Console
    py::class_<FullConsole, std::shared_ptr<FullConsole>>(mod, "Console")
        .def(py::init<>(&make_console), "cols"_a = 80, "rows"_a = 50,
             "font_file"_a = "", "tile_size"_a = Vec2i{0, 0},
             "font_size"_a = 16)
        .def("render", &FullConsole::render, "context"_a, "pos"_a = Vec2f(0, 0),
             "size"_a = Vec2f(-1, -1), "Render the console to the display")
        .def("put", &FullConsole::put, "pos"_a, "tile"_a, "Put char at position")
        .def("get", &FullConsole::get, "Get char at position")
        .def_readwrite("cursor_on", &FullConsole::cursor_on)
        .def_property("cursor_pos", &FullConsole::get_cursor,
                      &FullConsole::set_cursor)
        .def("get_tiles", &FullConsole::get_tiles)
        .def("set_tiles", &FullConsole::set_tiles, "tiles"_a)
        .def("clear", &FullConsole::clear)
        .def("set_color", &FullConsole::set_color)
        .def_property_readonly("grid_size", &FullConsole::get_size,
                               "Get number cols and rows")
        .def_property_readonly("tile_size", &FullConsole::get_tile_size,
                               "Get size of a single tile")
        .def("get_line", &FullConsole::read_line, "Enter line edit mode")
        .def("read_line", &FullConsole::read_line, "Enter line edit mode")
        .def("cancel_line", &FullConsole::stop_line, "Stop line edit mode")
        .def("set_line", &FullConsole::set_line, "Change the edited line")
        .def("get_font_image", &FullConsole::get_font_texture)
        .def("get_image_for", &FullConsole::get_texture_for_char, "tile"_a, "")
        .def(
            "write",
            [](FullConsole& con, std::vector<char32_t> const& data) {
                con.write(utf8::utf8_encode(data));
            },
            "tiles"_a)
        .def("write",
             static_cast<void (FullConsole::*)(std::string const&)>(
                 &FullConsole::write),
             "text"_a);
}
