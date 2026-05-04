import schemdraw
import schemdraw.logic as logic

with schemdraw.Drawing() as d:
    d += logic.And(inputs=2).color('blue')
    d += logic.Or().right().color('red')
    d += logic.Not().right().color('green')
    d.draw()