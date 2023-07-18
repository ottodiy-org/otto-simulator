from itertools import cycle

import motion
import ottosim
import zengl
from render import Renderer
from window import window

renderer = Renderer(zengl.context(), window.size)
animations = cycle([
    motion.balance,
    motion.walk,
    motion.dance,
    motion.turn_left,
    motion.turn_right,
    motion.jump,
])


class g:
    env = ottosim.make()
    animation = None
    t = None


def render():
    if g.t is None or g.t > 3.0:
        g.env.reset()
        g.t = 0.0
        g.animation = next(animations)

    for _ in range(5):
        g.t += 1.0 / 300.0
        action = g.animation(g.t)
        g.env.step(action)

    renderer.init((0.0, -0.3, 0.15), (0.0, 0.0, 0.07))
    renderer.render(g.env)
    renderer.flush()


window.on_frame = render
window.run()