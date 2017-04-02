import pyglet
from pyglet.window import key


class GameWindow(pyglet.window.Window):
  def __init__(self):
    super().__init__(visible=False, caption="PygletGame")

    self.label = pyglet.text.Label(
      '@',
      font_name='Helvetica Neue',
      font_size=36,
      x=self.width / 2,
      y=self.height / 2,
      anchor_x='center',
      anchor_y='center')
    self.set_location(0, 0)

  def on_draw(self):
    self.clear()
    self.label.draw()

  def on_key_press(self, symbol, modifiers):
    super().on_key_press(symbol, modifiers)
    if symbol == key.Q and modifiers | key.MOD_COMMAND:
      pyglet.app.exit()

    if symbol == key.LEFT:
      self.label.x -= 32
    if symbol == key.RIGHT:
      self.label.x += 32
    if symbol == key.UP:
      self.label.y += 32
    if symbol == key.DOWN:
      self.label.y -= 32


def main():
  window = GameWindow()
  window.set_visible()
  pyglet.app.run()
