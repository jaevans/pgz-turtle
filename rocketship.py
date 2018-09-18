import math



class TurtleActor(object):
    def __init__(self, *args, **kwargs):
        self.__dict__['_actor'] = Actor(*args, **kwargs)
        
    def __getattr__(self, attr):
        if attr in self.__dict__:
            return object.__getattribute__(self, attr)
        else:
            return getattr(self.__dict__['_actor'], attr)
            
    def __setattr__(self, attr, value):
        if attr in self.__dict__:
            return object.__setattribute__(self, attr, value)
        else:
            return setattr(self._actor, attr, value)
        
    def forward(self, distance):
        the_angle = math.radians(self._actor.angle)
        self._actor.x += distance * math.cos(the_angle)
        # We subtract the y as our y gets bigger heading downward
        self._actor.y -= distance * math.sin(the_angle)
        
    def backward(self, distance):
        self.forward(-distance)
        
    def left(self, angle):
        self._actor.angle += angle
    
    def right(self, angle):
        self._actor.angle -= angle
        
def draw():
    #screen.fill((173, 216, 230))
    screen.fill('lightblue')
    rocketship.draw()

def forward(actor, distance):
    the_angle = math.radians(actor.angle)
    actor.x += distance * math.cos(the_angle)
    # We subtract the y as our y gets bigger heading downward
    actor.y -= distance * math.sin(the_angle)

def backward(actor, distance):
    forward(actor, -distance)
    
def on_key_down(key):
    if key == keys.SPACE:
        rocketship.pos = rocketship.width / 2, rocketship.height / 2
        rocketship.angle = 0
    if key == keys.A:
        rocketship.angle = -45
        
def update():
    if keyboard[keys.LEFT]:
        rocketship.left(10)
    elif keyboard[keys.RIGHT]:
        rocketship.right(10)
    if keyboard[keys.UP]:
        rocketship.forward(10)
    elif keyboard[keys.DOWN]:
        rocketship.backward(10)
        
rocketship = TurtleActor('rocketship')
rocketship.angle = 0
WIDTH = 600 
HEIGHT = 600
trail = []