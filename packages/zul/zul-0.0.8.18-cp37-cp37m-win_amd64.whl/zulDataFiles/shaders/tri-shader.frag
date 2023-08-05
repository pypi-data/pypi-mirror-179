#version 450

layout (location = 0) out vec4 outColor;

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

float circle(in vec2 _st, in float _radius){
  vec2 dist = _st-vec2(0.5);
	return 1.-smoothstep(_radius-(_radius*0.01),
                         _radius+(_radius*0.01),
                         dot(dist,dist)*4.0);
}

vec2 u_resolution;

void main(){
  if (push.radius > 0) {
    // float radius = push.radius / push.windowWidth * 2 - 1;
    float dist = distance(gl_FragCoord.xy, vec2(push.x, push.y));
    if (dist > push.radius) {
      discard;
      return;
    }
  }

  outColor = vec4( push.color, 1.0 );
}
