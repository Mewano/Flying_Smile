import arcade


SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

def Draw_Face(x=300, y=300):
    radius = 200
    arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)


def Draw_Eye(x, y):
    radius = 20
    arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)


def Draw_Smile(x=300, y=280):
    width = 120
    height = 100
    start_angle = 190
    end_angle = 350
    arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)

def Draw_Entire_Image(x=300, y=300):
    Draw_Face(x, y)
    Draw_Eye(x+70, y+50)
    Draw_Eye(x-70, y+50)
    Draw_Smile(x, y-20)


class MyGame(arcade.Window):
    """ Главный класс приложения. """
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    a = 1
    b = 1

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        pass

    def on_draw(self):
        """ Отрендерить этот экран."""
        arcade.start_render()
        Draw_Entire_Image(self.x, self.y)

    def update(self, delta_time):
        arcade.finish_render()
        self.x += 12 * self.a
        self.y += 12 * self.b
        if (self.x >= SCREEN_WIDTH - 200):
            self.a *= -1
            self.x = SCREEN_WIDTH - 200
        elif (self.x <= 200):
            self.a *= -1
            self.x = 200
        if (self.y >= SCREEN_HEIGHT - 200):
            self.b *= -1
            self.y = SCREEN_HEIGHT - 200
        elif (self.y <= 200):
            self.b *= -1
            self.y = 200
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
