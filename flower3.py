from svg_backend import SVGBackend
from turtle import Turtle
from grammar import Grammar
from turtle import ThickTurtle
from turtle import NarrowingTurtle

grammar = Grammar()

grammar.add_non_terminal('Branch Right', [
    lambda turtle: turtle.forward(1.0),
    lambda turtle: turtle.turn_right(60)
])
grammar.add_non_terminal('Branch Left', [
    lambda turtle: turtle.forward(1.0),
    lambda turtle: turtle.turn_left(60)
])

grammar.add_non_terminal('Root', [
    'Tree',
    lambda turtle: turtle.turn_left(120),
    'Tree',
    lambda turtle: turtle.turn_left(120),
    'Tree',
])

scale = 0.5
grammar.add_non_terminal('Scale', [
    lambda turtle: turtle.scale(scale),
    lambda turtle: turtle.scale_thickness(0.6),
])
grammar.add_non_terminal('Scale', [])

grammar.add_non_terminal('Tree', [
    lambda turtle: turtle.store(),
    'Branch Left',
    'Scale',
    'Tree',
    lambda turtle: turtle.restore(),
    lambda turtle: turtle.store(),
    'Branch Right',
    'Scale',
    'Tree',
    lambda turtle: turtle.restore(),
], 8)

grammar.add_non_terminal('Tree', [])

for i in range(0, 5):
    backend = SVGBackend()
    turtle = ThickTurtle(backend)
    turtle.thickness = 0.05

    grammar.expand('Root', turtle, 12)
    backend.write('flower3/flower3_{:02}.svg'.format(i))
