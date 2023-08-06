#include "context.hpp"

namespace pix {

namespace gl = gl_wrap;
using gl::ProgramCache;

void Context::set_color(gl::Color const& col)
{
    fg = col;
}

void add_to(std::vector<float>& target, Vec2<float> const& v)
{
    target.push_back(v.x);
    target.push_back(v.y);
}

std::vector<float> Context::generate_circle(Vec2f const& center, float radius,
                                            bool include_center) const
{
    if (radius < 1) { return {}; }
    int steps = static_cast<int>(M_PI * 1.5 / asin(sqrt(1.0 / radius)));

    std::vector<float> vertexData;
    vertexData.reserve(steps + 2);

    if (include_center) { add_to(vertexData, to_screen(center)); }
    for (int i = 0; i <= steps; i++) {
        auto v = Vec2f::from_angle(M_PI * 2.0 * i / steps) * radius + center;
        add_to(vertexData, to_screen(v));
    }
    return vertexData;
}

std::array<float, 4> Context::generate_line(double x0, double y0, double x1,
                                            double y1)
{
    return {to_screen_x(x0 + 0.5), to_screen_y(y0 + 0.5), to_screen_x(x1 + 0.5),
            to_screen_y(y1 + 0.5)};
}

std::vector<float> Context::generate_lines(const float* screen_cords,
                                           int count) const
{
    std::vector<float> result;
    result.reserve(count * 2);
    for (int i = 0; i < count * 2; i += 2) {
        add_to(result, to_screen(screen_cords[i], screen_cords[i + 1]));
    }
    return result;
}

std::array<float, 8> Context::generate_quad(float x, float y, float w,
                                            float h) const
{
    float x0 = to_screen_x(x);
    float y0 = to_screen_y(y);
    float x1 = to_screen_x(x + w);
    float y1 = to_screen_y(y + h);
    return std::array{x0, y0, x1, y0, x1, y1, x0, y1};
}

std::array<float, 16> Context::generate_quad_with_uvs(Vec2f pos,
                                                      Vec2f size) const
{
    auto p0 = to_screen(pos);
    auto p1 = to_screen(pos + size);
    return std::array{p0.x, p0.y, p1.x, p0.y, p1.x, p1.y, p0.x, p1.y,
                      0.F,  1.F,  1.F,  1.F,  1.F,  0.F,  0.F,  0.F};
}

static Vec2f rotate(Vec2f v, float rot)
{
    auto ca = cosf(rot);
    auto sa = sinf(rot);
    return {v.x * ca - v.y * sa, v.x * sa + v.y * ca};
}

std::array<float, 8> Context::rotated_quad(Vec2f center, Vec2f sz,
                                           float rot) const
{
    sz = sz / 2;
    auto p0 = to_screen(rotate(Vec2f{-sz.x, -sz.y}, rot) + center);
    auto p1 = to_screen(rotate(Vec2f{sz.x, -sz.y}, rot) + center);
    auto p2 = to_screen(rotate(Vec2f{sz.x, sz.y}, rot) + center);
    auto p3 = to_screen(rotate(Vec2f{-sz.x, sz.y}, rot) + center);

    return std::array{p0.x, p0.y, p1.x, p1.y, p2.x, p2.y, p3.x, p3.y};
}

std::array<float, 16> Context::rotated_quad_with_uvs(Vec2f center, Vec2f sz,
                                                     float rot) const
{
    sz = sz / 2;
    auto p0 = to_screen(rotate(Vec2f{-sz.x, -sz.y}, rot) + center);
    auto p1 = to_screen(rotate(Vec2f{sz.x, -sz.y}, rot) + center);
    auto p2 = to_screen(rotate(Vec2f{sz.x, sz.y}, rot) + center);
    auto p3 = to_screen(rotate(Vec2f{-sz.x, sz.y}, rot) + center);

    return std::array{p0.x, p0.y, p1.x, p1.y, p2.x, p2.y, p3.x, p3.y,
                      0.F,  1.F,  1.F,  1.F,  1.F,  0.F,  0.F,  0.F};
}

void Context::filled_rect(float x, float y, float w, float h)
{
    draw_filled(generate_quad(x, y, w, h), gl::Primitive::TriangleFan);
}

void Context::rect(float x, float y, float w, float h)
{
    glLineWidth(line_width);
    draw_filled(generate_quad(x, y, w, h), gl::Primitive::LineLoop);
}

void Context::line(float x0, float y0, float x1, float y1)
{
    glLineWidth(line_width);
    draw_filled(generate_line(x0, y0, x1, y1), gl::Primitive::Lines);
    last_x = x1;
    last_y = y1;
}

void Context::line(float x1, float y1)
{
    glLineWidth(line_width);
    draw_filled(generate_line(last_x, last_y, x1, y1), gl::Primitive::Lines);
    last_x = x1;
    last_y = y1;
}

void Context::circle(Vec2f const& v, float r)
{
    glLineWidth(line_width);
    draw_filled(generate_circle(v, r, false), gl::Primitive::LineLoop);
}

void Context::filled_circle(Vec2f const& v, float r)
{
    draw_filled(generate_circle(v, r, true), gl::Primitive::TriangleFan);
}

void Context::blit(gl::TexRef const& tex, Vec2f pos, Vec2f size)
{
    tex.bind();
    if (size.x < 0) {
        size = {static_cast<float>(tex.width()),
                static_cast<float>(tex.height())};
    }
    // auto vdata = generate_quad_with_uvs(pos.x, pos.y, size.x, size.y);
    auto vdata = generate_quad_with_uvs(pos, size);
    std::copy(tex.uvs().begin(), tex.uvs().end(), vdata.begin() + 8);
    draw_textured(vdata, gl::Primitive::TriangleFan);
}

void Context::draw(gl::TexRef const& tex, Vec2f center, Vec2f size, float rot)
{
    tex.bind();
    if (size.x < 0) {
        size = {static_cast<float>(tex.width()),
                static_cast<float>(tex.height())};
    }
    // auto vdata = generate_quad_with_uvs(pos.x, pos.y, size.x, size.y);
    auto vdata = rotated_quad_with_uvs(center, size, rot);
    std::copy(tex.uvs().begin(), tex.uvs().end(), vdata.begin() + 8);
    draw_textured(vdata, gl::Primitive::TriangleFan);
}

Context::Context(Vec2f const& offs, Vec2f const& sz, GLuint fb)
    : target{fb}, offset{offs}, target_size{sz}, fg{color::white},
      colored{
          ProgramCache::get_instance()
              .get_program<ProgramCache::Colored, ProgramCache::NoTransform>()},
      textured{ProgramCache::get_instance()
                   .get_program<ProgramCache::Textured>()}, // NOLINT
      filled{ProgramCache::get_instance().get_program<>()}  // NOLINT
{
    // auto in_color = textured.getUniformLocation("in_color");
    // auto in_pos = textured.getAttribute("in_pos");
}

Context::Context(float w, float h, GLuint fb)
    : Context(Vec2f{0, 0}, Vec2f{w, h}, fb)
{
    static const std::array<float, 16> mat{1, 0, 0, 0, 0, 1, 0, 0,
                                           0, 0, 1, 0, 0, 0, 0, 1};
    gl::Color color = 0xffffffff;
    filled.setUniform("frag_color", color);
    filled.setUniform("in_transform", mat);
    textured.setUniform("frag_color", color);
    textured.setUniform("in_transform", mat);
}

/*
: target{fb}, target_size{w, h}, fg{color::white},
  colored{gl::ProgramCache::get_instance()
              .get_program<gl::ProgramCache::Colored,
                           ProgramCache::NoTransform>()},
  textured{gl::ProgramCache::get_instance()
               .get_program<gl::ProgramCache::Textured>()},
  filled{gl::ProgramCache::get_instance().get_program<>()}
{
static const std::array<float, 16> mat{1, 0, 0, 0, 0, 1, 0, 0,
                                       0, 0, 1, 0, 0, 0, 0, 1};
gl::Color color = 0xffffffff;
filled.setUniform("frag_color", color);
filled.setUniform("in_transform", mat);
textured.setUniform("frag_color", color);
textured.setUniform("in_transform", mat);
}
*/
template <typename CO>
void Context::draw_filled(const CO& container, gl_wrap::Primitive primitive)
{
    glBindFramebuffer(GL_FRAMEBUFFER, target);
    gl::setViewport({target_size.x * vpscale, target_size.y * vpscale});

    filled.use();
    filled.setUniform("frag_color", fg);
    auto pos = filled.getAttribute("in_pos");
    pos.enable();
    gl_wrap::ArrayBuffer<GL_STREAM_DRAW> vbo{container};
    vbo.bind();
    gl_wrap::vertexAttrib(pos, gl_wrap::Size<2>{}, gl_wrap::Type::Float,
                          0 * sizeof(GLfloat), 0);
    int len = static_cast<int>(container.size()) / 2;
    gl_wrap::drawArrays(primitive, 0, len);
    pos.disable();
}

void Context::set_target() const
{
    glBindFramebuffer(GL_FRAMEBUFFER, target);
    gl::setViewport({target_size.x * vpscale, target_size.y * vpscale});
}

template <typename CO>
void Context::draw_textured(const CO& container, gl_wrap::Primitive primitive)
{
    glBindFramebuffer(GL_FRAMEBUFFER, target);
    gl::setViewport({target_size.x * vpscale, target_size.y * vpscale});

    textured.use();
    textured.setUniform("frag_color", fg);
    auto pos = textured.getAttribute("in_pos");
    pos.enable();
    auto uv = textured.getAttribute("in_uv");
    uv.enable();
    gl_wrap::ArrayBuffer<GL_STREAM_DRAW> vbo{container};
    vbo.bind();
    int len = static_cast<int>(container.size()) / 2;
    gl_wrap::vertexAttrib(pos, gl_wrap::Size<2>{}, gl_wrap::Type::Float,
                          0 * sizeof(GLfloat), 0);
    gl_wrap::vertexAttrib(uv, gl_wrap::Size<2>{}, gl_wrap::Type::Float,
                          0 * sizeof(GLfloat), len * 4);

    gl_wrap::drawArrays(primitive, 0, len / 2);
    pos.disable();
    uv.disable();
}

void Context::clear(const gl_wrap::Color& col) const
{
    glBindFramebuffer(GL_FRAMEBUFFER, target);
    gl::setViewport({target_size.x * vpscale, target_size.y * vpscale});
    auto c = col.to_rgba();
    c &= clear_mask;
    gl_wrap::Color col2{c};
    glClearColor(col2.red, col2.green, col2.blue, col2.alpha);
    glClear(GL_COLOR_BUFFER_BIT);
}

std::vector<float> points;

void Context::plot(Vec2f point, gl_wrap::Color col)
{
    points.push_back(to_screen_x(point.x));
    points.push_back(to_screen_y(point.y));
    points.push_back(col.red);
    points.push_back(col.green);
    points.push_back(col.blue);
    points.push_back(col.alpha);

    if (points.size() > 32000) {
        draw_points();
        points.clear();
    }
}

void Context::draw_points()
{
    glBindFramebuffer(GL_FRAMEBUFFER, target);
    gl::setViewport({target_size.x * vpscale, target_size.y * vpscale});

    glPointSize(2.0);

    colored.use();
    auto pos = colored.getAttribute("in_pos");
    auto cola = colored.getAttribute("in_color");
    pos.enable();
    cola.enable();
    gl_wrap::ArrayBuffer<GL_STREAM_DRAW> vbo{points};
    vbo.bind();
    gl_wrap::vertexAttrib(pos, gl_wrap::Size<2>{}, gl_wrap::Type::Float,
                          6 * sizeof(GLfloat), 0);
    gl_wrap::vertexAttrib(cola, gl_wrap::Size<4>{}, gl_wrap::Type::Float,
                          6 * sizeof(GLfloat), 8);
    int len = static_cast<int>(points.size()) / 6;
    gl_wrap::drawArrays(gl_wrap::Primitive::Points, 0, len);
    pos.disable();
    cola.disable();
}
void Context::flush()
{
    if (!points.empty()) {
        draw_points();
        points.clear();
    }
}
} // namespace pix
