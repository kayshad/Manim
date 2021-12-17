from typing_extensions import runtime
from manim import *

class NumberLineExample(Scene):
    def construct(self):
        l0 = NumberLine(
            x_range=[-20, 20, 1],
            length=40,
            numbers_with_elongated_ticks=[0],
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
            font_size=12,
        )
        l1 = NumberLine(
            x_range=[-20, 20, 1],
            length=40,
            numbers_with_elongated_ticks=[0],
            color=RED,
            include_numbers=True,
            label_direction=DOWN,
            font_size=12,
        ).shift(DOWN*.5)


        line_group = VGroup(l0,l1)
        self.play(Create(line_group))
        self.play(l1.animate.shift(RIGHT),run_time=10)
        
