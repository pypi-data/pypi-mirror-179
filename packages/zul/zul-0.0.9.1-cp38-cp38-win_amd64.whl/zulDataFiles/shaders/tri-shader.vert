#version 450

layout(location = 0) in vec2 position;
layout(location = 1) in vec3 color;

layout(push_constant) uniform Push {
  mat2 transform;
  vec2 offset;
  vec3 color;
  float windowWidth;
  float windowHeight;
  float radius;
  float x;
  float y;
} push;

void main() {
    float x = position.x / push.windowWidth * 2 - 1;
    float y = position.y / push.windowHeight * 2 - 1;
    gl_Position = vec4(x, y, 0.0, 1.0);
}
