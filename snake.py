# slither
#slither game
#written by Dr.Mo, 1/20/2021(Jesse Madrigal)
import pygame#imports
import math#for square root
import random #for pellet locations

pygame.init()#initalizes pygame
screen = pygame.display.set_mode((400, 400))#game screen
pygame.display.set_caption("Slither")#window title
clock = pygame.time.Clock()#start game clock

#game variables
doExit = False

#player variables
xPos = 200
yPos = 200
Vx = 1
Vy = 1

oldx = 200
oldy = 200

xPos2 = 200
yPos2 = 200
Vx2 = 1
Vy2 = 1

oldx2 = 200
oldy2 = 200
#++++++++++++++++++++++++++++++++++++++++++++++++++
class tailSeg:
  def __init__(self, xpos, ypos):
    self.xpos = xpos
    self.ypos = ypos
  def update(self, xpos, ypos):
    self.xpos = xpos
    self.ypos = ypos
  def draw(self):
    pygame.draw.circle(screen, (200, 0, 0), (self.xpos, self.ypos), 12)

class pellet:
  def __init__(self, xpos, ypos, red, green, blue, radius):
    self.xpos = xpos
    self.ypos = ypos
    self.red = red
    self.green = green
    self.blue = blue
    self.radius = radius
  def draw(self):
    pygame.draw.circle(screen, (self.red, self.green, self. blue), (self.xpos, self.ypos), self.radius)
  def collide(self, x, y):
    if math.sqrt((x-self.xpos)**2 + (y-self.ypos)**2) < self.radius + 6:
      self.xpos = random.randrange(0,400)
      self.ypos = random.randrange(0,400)
      self.red = random.randrange(0,255)
      self.green = random.randrange(0,255)
      self.blue = random.randrange(0,255)
      self.radius = random.randrange(0,30)
      return True
#end class pellet++++++++++++++++++++++++++

pelletBag = list()#creates list data structure
tail = list()
tail2 = list()

counter = 0

#push 10 pellets into list
for i in range(10):
  pelletBag.append(pellet(random.randrange(0,400), random.randrange(0,400), random.randrange(0,255), random.randrange(0,255), random.randrange(0,255), random.randrange(0,30)))

#game loop#########################################
while not doExit:

#event/input section--------------------------------
  clock.tick(60)

  for event in pygame.event.get():#its like an cin for a mouse
    if event.type == pygame.QUIT:#lets you quit from gamescreen
      doExit == True
    if event.type == pygame.MOUSEMOTION:
      mousePos = event.pos

      if mousePos[0] > xPos:
        Vx = 1
      else:
        Vx = -1
      if mousePos[1] > yPos:
        Vy = 1
      else:
        Vy = -1
  #p2 keyboard movement
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
    yPos2-=1
  if keys[pygame.K_s]:
    yPos2+=1
  if keys[pygame.K_a]:
    xPos2-=1
  if keys[pygame.K_d]:
    xPos2+=1
    
#physics section--------------------------------------
  #update circle position
  xPos += Vx
  yPos += Vy
 

  if xPos < 10 or xPos > 390 or yPos < 10 or yPos > 390:
    doExit = True
  if xPos2 < 10 or xPos2 > 390 or yPos2 < 10 or yPos2 > 390:
    doExit = True

  counter+=1#update counter
  if counter == 20:#create a delay so segments follow 
    counter = 0#resets counter
    oldx = xPos#holds onto position from 20 ticks ago
    oldy = yPos
    oldx2 = xPos2
    oldy2 = yPos2

    if(len(tail)>2):#dont push numbers if theres no nodes
      for i in range(len(tail)):#loop for each list slot
        #start in las position, push the *second to last* into it, repeat till at beginning
        tail[len(tail)-i-1].xpos = tail[len(tail)-i-2].xpos
        tail[len(tail)-i-1].ypos = tail[len(tail)-i-2].ypos
    

    if(len(tail2)>2):#dont push numbers if theres no nodes
      for i in range(len(tail2)):#loop for each list slot
        #start in las position, push the *second to last* into it, repeat till at beginning
        tail2[len(tail2)-i-1].xpos = tail2[len(tail2)-i-2].xpos
        tail2[len(tail2)-i-1].ypos = tail2[len(tail2)-i-2].ypos
    if(len(tail2)>0):#if you have at least one segment, push old head segment into that
      tail2[0].update(oldx2, oldy2)#push head position into first position of list
    if(len(tail)>0):#if you have at least one segment, push old head segment into that
      tail[0].update(oldx, oldy)#push head position into first position of list


  for i in range(10):
    if pelletBag[i].collide(xPos, yPos) == True:
      tail.append(tailSeg(oldx, oldy))
    if pelletBag[i].collide(xPos2, yPos2) == True:
      tail2.append(tailSeg(oldx2, oldy2))


#render section----------------------------------------
  screen.fill((255,255,255))#clears screen, needed to prevent smear

  pygame.draw.circle(screen, (200, 0, 200), (xPos, yPos), 12)

  pygame.draw.circle(screen, (0, 200, 200), (xPos2, yPos2), 12)

  for i in range(10):
    pelletBag[i].draw()

  for i in range (len(tail)):
    tail[i].draw()

  for i in range (len(tail2)):
    tail2[i].draw()

  pygame.display.flip()


#end game loop######################################

pygame.quit()
