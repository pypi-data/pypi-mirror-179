#pragma once

#include "../colors.hpp"
#include "../gl/texture.hpp"
#include "../machine.hpp"
#include "../vec2.hpp"
#include "full_console.hpp"

#include <optional>
#include <pybind11/detail/common.h>
#include <pybind11/pybind11.h>

#include <string>
#include <tuple>

using namespace pybind11::literals;

namespace py = pybind11;
namespace gl = gl_wrap;

inline std::shared_ptr<pix::Context> make_context(Vec2f size)
{
    if (size.x == 0 && size.y == 0) {
        size = Vec2f{Machine::get_instance().screen->get_size()};
    }
    return std::make_shared<pix::Context>(size.x, size.y);
}

inline pix::Context* context_from(gl::TexRef& tr)
{
    if (tr.data != nullptr) {
        return static_cast<pix::Context*>(tr.data.get());
    }

    auto* context = new pix::Context(
        {static_cast<float>(tr.x()), static_cast<float>(tr.y())},
        {static_cast<float>(tr.tex->width), static_cast<float>(tr.tex->height)},
        tr.get_target());
    tr.data = std::shared_ptr<void>(static_cast<void*>(context), [](void* ptr) {
        delete static_cast<pix::Context*>(ptr);
    });
    return context;
}

inline pix::Context* context_from(Screen& screen)
{
    return Machine::get_instance().context.get();
}

inline pix::Context* context_from(pix::Context& context)
{
    return &context;
}

template <typename T, typename... O>
inline void add_draw_functions(pybind11::class_<T, O...>& cls)
{
    // clang-format off
    cls.def("circle", [](T& self, Vec2f const& center, float r) {
      context_from(self)->circle(center, r);
    }, "center"_a, "radius"_a);

    cls.def("filled_circle", [](T& self, Vec2f const& center, float r) {
      context_from(self)->filled_circle(center, r);
    }, "center"_a, "radius"_a);

    cls.def("line", [](T& self, Vec2f const& from, Vec2f const& to) {
      context_from(self)->line(from, to);
    }, "start"_a, "end"_a);

    cls.def("line", [](T& self, Vec2f const& to) {
      context_from(self)->line(to);
    }, "end"_a);

    cls.def("plot", [](T& self, Vec2f const& to, uint32_t color) {
      context_from(self)->plot(to, gl_wrap::Color(color));
    }, "center"_a, "color"_a);

    cls.def("rect", [](T& self, Vec2f const& xy, Vec2f const& size) {
      context_from(self)->rect(xy, size);
    }, "top_left"_a, "size"_a);

    cls.def("filled_rect", [](T& self, Vec2f const& xy, Vec2f const& size) {
      context_from(self)->filled_rect(xy, size);
    }, "top_left"_a, "size"_a);

    cls.def("draw", [](T& self, gl_wrap::TexRef const& tr,
                       std::optional<Vec2f> xy, std::optional<Vec2f> center,
                       Vec2f size, float rot) {
            pix::Context* ctx = context_from(self);
            if (center) {
                ctx->draw(tr, *center, size, rot);
            } else if (xy) {
               ctx->blit(tr, *xy, size); 
            } else {
               ctx->blit(tr, {0,0}, size); 
            }
            }, "image"_a, "top_left"_a = std::nullopt,
            "center"_a = std::nullopt,
            "size"_a = Vec2f{-1, -1}, "rot"_a = 0);
    cls.def("draw", [](T& self, FullConsole& con,
                       Vec2f const& xy, Vec2f const& size) {
                con.render(context_from(self), xy, size);
            }, "drawable"_a, "top_left"_a = Vec2f{0, 0},
            "size"_a = Vec2f{-1, -1});
    cls.def("blit", [](T& self, gl_wrap::TexRef const& tr,
                       Vec2f const& xy, Vec2f const& size) {
              context_from(self)->blit(tr, xy, size);
            }, "image"_a, "top_left"_a = Vec2f{0, 0},
            "size"_a = Vec2f{-1, -1});
    cls.def( "clear", [](T& self, uint32_t color) {
      context_from(self)->clear(color);
    }, "color"_a = color::transp);
    cls.def_property("draw_color", [](T& self) {
      return context_from(self)->fg.to_rgba();
    }, [](T& self, uint32_t color) {
      context_from(self)->set_color(color);
    });
    cls.def_property("line_width", [](T& self) {
      return context_from(self)->line_width;
    }, [](T& self, float lw) {
      context_from(self)->line_width = lw;
    });
    cls.def_property_readonly(
        "context", [](T& tr) { return context_from(tr); });
    // clang-format on
}
inline auto add_context_class(py::module_ const& mod)
{
    return py::class_<pix::Context, std::shared_ptr<pix::Context>>(mod,
                                                                   "Context")
        .def(py::init<>(&make_context), "size"_a = Vec2f{0, 0});
}
