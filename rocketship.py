import math

rocketship = Actor('rocketship')
rocketship.angle = 0
WIDTH = 300
HEIGHT = 300


def draw():
    #screen.fill((173, 216, 230))
    screen.fill('lightblue')
    rocketship.draw()

def forward(actor, distance):
    the_angle = math.radians(actor.angle+90)
    print(the_angle)
    print("dx, dy = ({},{})".format(math.cos(the_angle), math.sin(the_angle)))
    actor.x += distance * math.cos(the_angle)
    actor.y += distance * math.sin(the_angle)
    
def on_key_down(key):
    print(key)
    if key == keys.SPACE:
        rocketship.pos = rocketship.width / 2, rocketship.height / 2
        rocketship.angle = 0
    if key == keys.A:
        rocketship.angle = -45
        
def update():
    if keyboard[keys.LEFT]:
        rocketship.angle += 2
    elif keyboard[keys.RIGHT]:
        rocketship.angle -= 2
    if keyboard[keys.UP]:
        forward(rocketship,10)