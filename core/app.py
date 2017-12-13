import sys
import pygame as pg
from .settings import *
from .ui import *
from .graph import Graph


class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption(CAPTION)
        self.screen = pg.display.set_mode(SIZE, 0, 32)
        self.clock = pg.time.Clock()

        # UI
        self.instructions = Button("Instructions", (100, 30), (10, 10))
        self.instructions.on_click(self.show_instructions)
        self.settings = Button("Settings", (100, 30), (10, 50))
        self.settings.on_click(self.show_settings)
        self.sett, self.inst = False, False

        # Navigation Graph
        self.graph = Graph((600, 500), (50, 150))

    def show_instructions(self):
        self.inst = not self.inst

    def show_settings(self):
        self.sett = not self.sett

    def run(self):

        while True:
            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                self.settings.event(ev)
                self.instructions.event(ev)
                self.graph.event(ev)

            # Draw
            self.screen.fill(BACKGROUND)

            draw_header(self.screen)
            self.graph.draw(self.screen)

            self.instructions.draw(self.screen)
            self.settings.draw(self.screen)
            if self.inst:
                draw_instructions(self.screen)
            if self.sett:
                draw_settings(self.screen)


            pg.display.flip()

            # Update
            dt = self.clock.tick(FPS) / 1000.0
            self.graph.update(dt)
