from tkinter import * 
import random 
import time 


class Game(object):
  def __init__(self): 
    self.tk = Tk()
    self.tk.title('Game1')
    self.canvas = Canvas(self.tk, width = 500, height = 500, highlightthickness=0)
    self.canvas.pack()
    self.tk.update()
    self.tk.resizable(0, 0)
    self.canvas_height = 500 
    self.canvas_width = 500 
    self.bg = PhotoImage(file='what.jpg')
    w = self.bg.width()
    h = self.bg.height()
    for x in range(0, 5): 
      for y in range(0, 5): 
        self.canvas.create_image(x*w, y*h, image = self.bg, anchor = 'nw')
    self.sprites = []
    self.running = True
  def Mainloop(self): 
    while True:
        if self.running == True:
          for i in self.sprites:
            i.move()
        self.tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

class Coords():
  def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0): 
    self.x1 = x1
    self.x2 = x2
    self.y1 = y1
    self.y2 = y2
  def within_x(co1, co2):
    if co1.x1 > co2.x1 and co1.x1 < co2.x2:
      return True
    elif co1.x2 > co2.x1 and co1.x2 < co2.x2:
      return True
    elif co2.x1 > co1.x1 and co2.x1 < co1.x2:
      return True
    elif co2.x2 > co1.x1 and co2.x2 < co1.x2: 
      return True   
    else:
      return False
  def within_y(co1, co2):
    if co1.y1 > co2.y1 and co1.y1 < co2.y2:
      return True
    elif co1.y2 > co2.y1 and co1.y2 < co2.y2:
      return True
    elif co2.y1 > co1.y1 and co2.y1 < co1.y2:
      return True
    elif co2.y2 > co1.y1 and co2.y2 < co1.y2: 
      return True   
    else:
      return False
  def collided_left(co1, co2):
    if within_y(co1, co2):
      if co1.x1 <= co2.x2 and co1.x1 >= co2.x1:
        return True
    return False
  def collided_right(co1, co2): 
    if within_y(co1, co2):
      if co1.x2 >= co2.x1 and co1.x2 <= co2.x2:
        return True
    return False
  def collided_top(co1, co2): 
    if within_x(co1, co2): 
      if co1.y1 <= co2.y2 and co1.y1 >= co2.y1: 
        return True
    return False
  def collided_bottom(co1, co2, y_calc): 
    if within_x(co1, co2): 
      y_calc = co1.y2 + y1
      if y_calc >= co2.y1 and y_calc <= co2.y2:
        return True
    return False

class Sprite(): 
  def __init__(self, game): 
    self.game = game
    self.endgame = False
    self.coordinates = None
  
  def move(self): 
    pass
  def coords(self):
    return self.coordinates

class PlatformSprite(Sprite):
  def __init__(self, game, PhotoImage, x, y, width, height):
    pass 

tk.update()
tk.update_idletasks()
time.sleep(0.01)
