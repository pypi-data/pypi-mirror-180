from tkinter import Tk, Canvas
from time import sleep, time
from keyboard import is_pressed
import pgengine.matrix as matrix
from math import hypot, radians, degrees, sqrt
from copy import copy
# import tkinter

class Color:
    BLACK = '#000'
    WHITE = '#fff'
    GRAY = '#888'
    RED = '#f00'
    GREEN = '#0f0'
    BLUE = '#00f'
    YELLOW = '#ff0'
    VIOLET = '#f0f'
    LIGHTBLUE = '#0ff'

def _empty():
    pass

def sign(n):
    if n == 0:
        return 1
    return n / abs(n)

class scene:
    '''
    This is scene class. It contains all information about:
    -window(window width and height, that you can change)
    -all entities on the scene
    -FPS
    -etc.
    '''
    def __init__(self):
        self.running = True
        
        self.all_entities = []
        self.ui = []

        self.FPS = 120
        self.unit = 50
        
        self.g = 9.8
        self.defaultCollider = False
        self.width, self.height = 1000, 800
        
        self.def_width, self.def_height = self.width, self.height
        
        self.tk = Tk()
        self.tk.title('Window')
        
        self.canvas = Canvas(width = self.width, height = self.height, bg = Color.BLACK, highlightthickness=0)
        self.canvas.pack()
    def background(self, color):
        self.canvas.configure(bg = color)
    def title(self, name):
        self.tk.title(name)
    def tick(self, time1, time2, FPS):
        sleep(time2-time1+1/FPS)
    def fullscreen(self, state:bool = True):
        '''
        Enter or exit fullscreen mode.

        :param state: Enter or exit fullscreen variable.
        :type state: bool
        '''
        if state:
            self.tk.attributes('-fullscreen', True)
            screen_width = self.tk.winfo_screenwidth()
            screen_height = self.tk.winfo_screenheight()
            self.setSize(screen_width, screen_height, defValue = False)
        else:
            self.tk.attributes('-fullscreen', False)
            self.setSize(self.def_width, self.def_height)
    def run(self, update = _empty):
        while self.running:
            engine_update(update)
    def refresh(self):
        self.tk.update_idletasks()
        self.tk.update()
        self.canvas.delete('all')
    def setSize(self, width: int, height: int, defValue: bool = True):
        '''
        Seting a size of window to specified width and height

        :type width: int
        :type height: int
        '''
        if defValue:
            self.def_width, self.def_height = width, height
        self.width, self.height = width, height
        self.canvas.configure(width = width, height = height)

Scene = scene()

class InputManager:
    left_down = False
    right_down = False
    def initialisate():
        Scene.canvas.bind("<Button-1>", InputManager.left_go_down)
        Scene.canvas.bind("<ButtonRelease-1>", InputManager.left_go_up)
    def left_go_down(evt):
        InputManager.left_down = True
    def left_go_up(evt):
        InputManager.left_down = False
    def getMouseButton(btn = 0):
        if btn == 0:
            return InputManager.left_down
        elif btn == 1:
            return InputManager.right_down
    def keyDown(key):
        '''
        :return: is key pressed
        '''
        return is_pressed(key)
    def mousePos():
        '''
        :return: mouse position
        '''
        mouse_x = (Scene.tk.winfo_pointerx() - Scene.tk.winfo_rootx() - Scene.width//2) / Scene.unit
        mouse_y = (Scene.tk.winfo_pointery() - Scene.tk.winfo_rooty() - Scene.height//2) / Scene.unit
        return mouse_x, mouse_y

class Vector:
    def normalise(self):
        '''
        This method normalising vector
        '''
        max_n = max(abs(self.x), abs(self.y))
        if max_n != 0:
            self.x, self.y = self.x / max_n, self.y / max_n
        return self
    def normalised(self):
        '''
        This method normalising vector
        '''
        max_n = max(abs(self.x), abs(self.y))
        if max_n != 0:
            return Vector(self.x / max_n, self.y / max_n)
        return self
        
    def getMatrixPosition(self):
        '''
        :return: vector position in matrix style
        '''
        return (self.x, ), (self.y, )
    def __init__(self, x  = 0, y = 0, angle = 0):
        self.x = x
        self.y = y
        self.angle = angle
    def __add__(self, other):
        if type(other) == Vector:
            x = self.x + other.x
            y = self.y + other.y
            return Vector(x, y)
    def __radd__(self, other):
        return self.__add__(other)
    def __repr__(self) -> tuple:
        return (self.x, self.y)
    def __mul__(self, other):
        if type(other) == Vector:
            x = self.x * other.x
            y = self.y * other.y
            return Vector(x, y)
        if type(other) in [int, float]:
            x = self.x * other
            y = self.y * other
            return Vector(x, y)
    def __rmul__(self, other):
        return self.__mul__(other)
    def __truediv__(self, other):
        if type(other) == Vector:
            x = self.x / other.x
            y = self.y / other.y
            return Vector(x, y)
        if type(other) in [int, float]:
            x = self.x / other
            y = self.y / other
            return Vector(x, y)
    def __rtruediv__(self, other):
        if type(other) == Vector:
            x = other.x / self.x
            y = other.y / self.y
            return Vector(x, y)
        if type(other) in [int, float]:
            x = other / self.x
            y = other / self.y
            return Vector(x, y)
    def __sub__(self, other):
        if type(other) == Vector:
            x = self.x - other.x
            y = self.y - other.y
            return Vector(x, y)
    def __rsub__(self, other):
        return self.__sub__(other)
    def __str__(self):
        return str(self.x) + ', ' + str(self.y)
class Entity:
    def __init__(self, pos = None, rot = 0, color: str = Color.WHITE, tag = None, mass = 5, drawable = True, usable = True, anchorX = Scene.width//2, anchorY = Scene.height//2):
        if type(pos) == tuple:
            pos = Vector(pos[0], pos[1])
        self.position = pos
        self.rotation = rot
        self.color = color
        self.last_rotation = 0

        self.drawable = drawable
        self.usable = usable

        self.collider_shape = None
        self.tag = tag

        self.orientation = Vector(0, 1)
        self.forward = self.orientation
        self.left = Vector(-1, 0)
        self.right = Vector(1, 0)
        self.back = Vector(0, -1)
        self.anchorX = anchorX
        self.anchorY = anchorY
        # rotated = matrix.multiply(matrix.rotation(self.rotation), self.forward.getMatrixPosition())
        # self.forward.x, self.forward.y = rotated[0][0], rotated[1][0]
        # self.last_rotation = self.rotation

        self.collider = Scene.defaultCollider
        self.rigidbody = False
        self.collided = False
        self.colliding_objects = 'all'

        self.accX = 0
        self.accY = 0
        self.velX = 0
        self.velY = 0

        self.move_y = None

        self.have_gravity = False

        self.mass = mass

        Scene.all_entities.append(self)
    def update(self):
        # self.last_rotation = self.rotation
        if self.collider and self.colliding_objects == 'all':
            for _entity in Scene.all_entities:
                if _entity != self and _entity.collider and self.collision(_entity):
                    self.collided = True
                    break
                self.collided = False
        if self.have_gravity:
            if not self.collided:
                self.gravity()
        
        # if self.have_gravity and not self.collided:
        #     gravity_casts = []
        #     verticies_g = []
        #     last_v = Vector(0, 0)
        #     for v in self.verticies:
        #         if v.y >= last_v.y and len(gravity_casts) < 3:
        #             ray = raycaster.ray(v + self.position, Vector(0, 1))
                    
        #             gravity_casts.append(ray)
        #             verticies_g.append(v)
        #             last_v = v
        #     rays_y = [ray.y for ray in gravity_casts if ray != None]
        #     # print(len(rays_y))
        #     if len(rays_y) and not self.collided:
        #         # print(';bssj')
        #         self.move_y = min(rays_y)
        #         index = rays_y.index(self.move_y)
        #         v = verticies_g[index]
        #         self.move_y -= v.y - 1/Scene.unit
        
        # if self.collided and self.velY > 0:
        #     self.accY = 0
        #     self.velY = 0
        self.velX += self.accX
        self.velY += self.accY

        self.position.x += self.velX
        self.position.y += self.velY

        self.accX = 0
        self.accY = 0
        # if self.have_gravity:
        if self.collider and self.colliding_objects == 'all':
            for _entity in Scene.all_entities:
                if _entity != self and _entity.collider and self.collision(_entity):
                    self.collided = True
                    break
                self.collided = False

        if self.collided and self.move_y != None:
            self.position.y = self.move_y
            self.move_y = None
        
        if self.collider_shape == 'polygon':
            for v in self.verticies:
                rotated = matrix.multiply(matrix.rotation(self.rotation - self.last_rotation), v.getMatrixPosition())
                v.x, v.y = rotated[0][0], rotated[1][0]
        rotated = matrix.multiply(matrix.rotation(self.rotation - self.last_rotation), self.orientation.getMatrixPosition())
        self.orientation.x, self.orientation.y = rotated[0][0], rotated[1][0]
        self.last_rotation = self.rotation

        self.forward = self.orientation
        self.back = Vector(-self.forward.x, -self.forward.y)
        self.left = Vector(self.forward.y, -self.forward.x)
        self.right = Vector(-self.left.x, -self.left.y)
        
        if self.drawable: self.draw()
    def gravity(self):
        if not self.collided:
            self.force((0, self.mass / 1000 * Scene.g))
    def force(self, pos):
        if type(pos) == tuple:
            x, y = pos
        if type(pos) == Vector:
            x, y = pos.x, pos.y
        
        fX = x / Scene.unit * 10
        fY = y / Scene.unit * 10
        self.accX += fX
        self.accY += fY
    def circle_polygon_collision(circle, polygon):
        for i, v in enumerate(polygon.verticies):
            A = v
            B = copy(polygon.verticies[(i+1) % len(polygon.verticies)])

            linePt = None
        
            x1 = (A.x + polygon.position.x)
            y1 = (-A.y - polygon.position.y)
            x2 = (B.x + polygon.position.x)
            y2 = (-B.y - polygon.position.y)

            direction = (B - A)
            direction.x, direction.y = direction.y, direction.x

            x3 = circle.position.x 
            y3 = -circle.position.y
            x4 = (circle.position.x + direction.x)
            y4 = (-circle.position.y + direction.y)

            den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if (den == 0):
                continue
            
            t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
            u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
            if 1 > t > 0 and 1 > u > 0:
                linePt = Vector()
                linePt.x = (x1 + t * (x2 - x1))
                linePt.y = (y1 + t * (y2 - y1))
            
            if linePt == None:
                distA = sqrt((x1 - circle.position.x) ** 2 + (y1 + circle.position.y) ** 2)
                distB = sqrt((x2 - circle.position.x) ** 2 + (y2 + circle.position.y) ** 2)
                if distA <= circle.radius or distB <= circle.radius:
                    return True
                continue

            pt = linePt
            
            if hypot(pt.x - circle.position.x, pt.y + circle.position.y) <= circle.radius:
                return True
    def collision(self, other):
        if self.collider_shape == 'polygon':
            if other.collider_shape == 'polygon':
                for i, v1 in enumerate(other.verticies):
                    x1 = (-v1.x + other.position.x)
                    y1 = v1.y + other.position.y
                    x2 = (-other.verticies[(i+1) % 4].x + other.position.x)
                    y2 = other.verticies[(i+1) % 4].y + other.position.y

                    for j, v2 in enumerate(self.verticies):
                        x3 = -v2.x + self.position.x
                        y3 = v2.y + self.position.y
                        x4 = -self.verticies[(j+1) % 4].x + self.position.x
                        y4 = self.verticies[(j+1) % 4].y + self.position.y

                        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
                        if (den == 0):
                            continue

                        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den;
                        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den;
                        if 1 > t > 0 and 1 > u > 0:
                            pt = Vector()
                            pt.x = x1 + t * (x2 - x1)
                            pt.y = y1 + t * (y2 - y1)
                            if self.rigidbody:
                                normal = Vector(y2 - y1, -(x2 - x1))
                                normal.normalise()
                                
                                vert = copy(v2)
                                vert.y *= -1
                                # vert.x *= -1
                                vert += self.position
                                pt = vert
                                # Scene.canvas.create_oval(pt.x * Scene.unit - 5 + Scene.width//2, pt.y * Scene.unit - 5 + Scene.height//2, pt.x * Scene.unit + 5 + Scene.width//2, pt.y * Scene.unit + 5 + Scene.height//2, fill = 'yellow')
                                
                                hit = raycaster.ray(vert, normal, [other])
                                if sign(self.velX) == -sign(normal.x):
                                    self.velX = 0
                                if sign(self.velY) == -sign(normal.y):
                                    self.velY = 0
                                
                                if hit:
                                    # hit.x *= -1
                                    self.position += hit - vert
                                # print(hit, vert)
                                # if normal.x and normal.y:
                                #     self.position += Vector(1 / Scene.unit * abs(normal.x) / normal.x, 1 / Scene.unit * abs(normal.y) / normal.y)
                                # elif not normal.x:
                                #     self.position += Vector(1 / Scene.unit * normal.x, 1 / Scene.unit * abs(normal.y) / normal.y)
                                # elif not normal.y:
                                #     self.position += Vector(1 / Scene.unit * abs(normal.x) / normal.x, 1 / Scene.unit * normal.y)
                            return True
            elif other.collider_shape == 'circle':
                return Entity.circle_polygon_collision(other, self)
        if self.collider_shape == 'circle':
            if other.collider_shape == 'circle':
                dist = hypot(other.position.x - self.position.x, other.position.y - self.position.y)
                if dist <= other.radius + self.radius:
                    return True
            elif other.collider_shape == 'polygon':
                return Entity.circle_polygon_collision(self, other)
class Polygon(Entity):
    def __init__(self, pos = copy(Vector(0, 0)), rot = 0, scale = None, color: str = Color.WHITE, tag = None, mass = 5, drawable = True, usable = True):
        super().__init__(pos, rot, color, tag, mass, drawable, usable)
        if not scale:
            scale = Vector(1, 1)
        elif type(scale) == tuple:
            scale = Vector(scale[0], scale[1])
        self.scale = scale
        self.collider_shape = 'polygon'

        self.verticies = [Vector(x, y) for x in [-scale.x/2, scale.x/2] for y in [-scale.y/2, scale.y/2]]
        self.verticies[2], self.verticies[3] = self.verticies[3], self.verticies[2]
    def draw(self):
        draw_verticies = [pos2 for pos in self.verticies for pos2 in pos.__repr__()]
        for i in range(len(draw_verticies)):
            if i % 2:
                draw_verticies[i] += self.position.y
            else:
                draw_verticies[i] += self.position.x
            draw_verticies[i] *= Scene.unit
            if i % 2:
                draw_verticies[i] += self.anchorY
            else:
                draw_verticies[i] += self.anchorX
        Scene.canvas.create_polygon(draw_verticies, fill = self.color)
class Circle(Entity):
    def __init__(self, pos = copy(Vector(0, 0)), rot = 0, radius = 0.5, color: str = Color.WHITE, tag = None, mass = 5, drawable = True):
        super().__init__(pos, rot, color, tag, mass, drawable)
        self.radius = radius
        self.collider_shape = 'circle'
    def draw(self):
        Scene.canvas.create_oval((self.position.x - self.radius) * Scene.unit + self.anchorX, (self.position.y - self.radius)  * Scene.unit + self.anchorY, (self.position.x + self.radius) * Scene.unit + self.anchorX, (self.position.y + self.radius) * Scene.unit + self.anchorY, fill = self.color, outline = '')
class Line(Entity):
    def __init__(self, start = copy(Vector(0, 0)), end=copy(Vector(0, 0)), rot=0, color: str = Color.WHITE, tag=None, mass=5, drawable=True, width = 3):
        if type(start) == tuple:
            start = Vector(start[0], start[1])
        if type(end) == tuple:
            end = Vector(end[0], end[1])
        super().__init__(start - end, rot, color, tag, mass, drawable)
        self.start = start
        self.end = end
        self.width = width
    def draw(self):
        Scene.canvas.create_line(self.start.x * Scene.unit + self.anchorX, self.start.y * Scene.unit + self.anchorY, self.end.x * Scene.unit + self.anchorX, self.end.y * Scene.unit + self.anchorY, width = self.width, fill = self.color)

class Text:
    def __init__(self, pos = copy(Vector(0, 0)), size = 1, text = '', color = 'black'):
        if type(pos) == tuple:
            pos = Vector(pos[0], pos[1])
        self.position = pos
        self.text = text
        self.color = color
        self.size = size

        self.drawable = True

        Scene.ui.append(self)
    def update(self):
        self.draw()
    def draw(self):
        Scene.canvas.create_text(self.position.x * Scene.unit + self.anchorX, self.position.y * Scene.unit + self.anchorY, text = self.text, fill = self.color, font = ('Times', int(self.size * Scene.unit)))

class Button:
    def __init__(self, pos = copy(Vector(0, 0)), scale = copy(Vector(1, 1)), text = '', text_color = Color.BLACK, color = Color.WHITE, outline_color = '', highlight_color = 'white', onclick = _empty, onrelease = _empty, whileclicked = _empty, anchorX = Scene.width//2, anchorY = Scene.height//2):
        if type(pos) == tuple:
            pos = Vector(pos[0], pos[1])
        if type(scale) == tuple:
            scale = Vector(scale[0], scale[1])
        self.position = pos
        self.text = text
        self.color = color
        self.outline_color = outline_color
        self.highlight_color = highlight_color
        self.text_color = text_color
        self.scale = scale
        self.onclick = onclick
        self.onrelease = onrelease
        self.whileclicked = whileclicked
        self.clicked = False
        self.anchorX = anchorX
        self.anchorY = anchorY

        self.drawable = True
        self.usable = True

        Scene.all_entities.append(self)
    def draw(self):
        color = self.color
        if self.clicked:
            color = self.highlight_color
        Scene.canvas.create_rectangle((self.position.x - self.scale.x/2) * Scene.unit + self.anchorX, (self.position.y - self.scale.y/2) * Scene.unit + self.anchorY, (self.position.x + self.scale.x/2) * Scene.unit + self.anchorX, (self.position.y + self.scale.y/2) * Scene.unit + self.anchorY, fill = color, outline = self.outline_color)
        Scene.canvas.create_text(self.position.x * Scene.unit + self.anchorX, self.position.y * Scene.unit + self.anchorY, text = self.text, fill = self.text_color, font = ('Times', int(0.5 * Scene.unit)))
    def update(self):
        mouse_x, mouse_y = InputManager.mousePos()
        if InputManager.getMouseButton(0):
            if self.clicked:
                self.whileclicked()
            if self.position.x - self.scale.x/2 < mouse_x < self.position.x + self.scale.x/2 and self.position.y - self.scale.y/2 < mouse_y < self.position.y + self.scale.y/2:
                # self.whileclicked()
                if not self.clicked:
                    self.onclick()
                self.clicked = True
        else:
            if self.clicked:
                self.onrelease()
            self.clicked = False
        self.draw()

# class InputField:
#     def __init__(self, pos = copy(Vector(0, 0)), scale = copy(Vector(1, 1)), text = '', text_color = Color.BLACK, color = Color.WHITE, highlight_color = 'white', command = _empty):
#         if type(pos) == tuple:
#             pos = Vector(pos[0], pos[1])
#         if type(scale) == tuple:
#             scale = Vector(scale[0], scale[1])
#         self.position = pos
#         self.text = text
#         self.color = color
#         self.highlight_color = highlight_color
#         self.text_color = text_color
#         self.scale = scale
#         self.onclick = command
#         self.clicked = False

#         self.drawable = True

#         Scene.ui.append(self)
#     def draw(self):
#         color = self.color
#         if self.clicked:
#             color = self.highlight_color
#         Scene.canvas.create_rectangle((self.position.x - self.scale.x/2) * Scene.unit + self.anchorX, (self.position.y - self.scale.y/2) * Scene.unit + Scene.height/2, (self.position.x + self.scale.x/2) * Scene.unit + Scene.width/2, (self.position.y + self.scale.y/2) * Scene.unit + Scene.height/2, fill = color, outline = '')
#         Scene.canvas.create_text(self.position.x * Scene.unit + Scene.width/2, self.position.y * Scene.unit + Scene.height/2, text = self.text, fill = self.text_color, font = ('Times', int(0.5 * Scene.unit)))
#     def update(self):
#         pass

class Raycast:
    def ray(self, start_point: Vector, dir: Vector, objects = Scene.all_entities):
        '''
        :return: ray hit point
        '''
        dir.normalise()
        x3 = -start_point.x
        y3 = start_point.y
        x4 = -start_point.x + dir.x
        y4 = start_point.y + dir.y

        last_pt = None

        for other in objects:
            for i, v1 in enumerate(other.verticies):
                x1 = -(v1.x + other.position.x)
                y1 = v1.y + other.position.y
                x2 = -(other.verticies[(i+1) % 4].x + other.position.x)
                y2 = other.verticies[(i+1) % 4].y + other.position.y


                den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
                if (den == 0):
                    continue

                t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
                u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
                if 1 > t > 0 and u > 0:
                    pt = Vector()
                    pt.x = x1 + t * (x2 - x1)
                    pt.y = y1 + t * (y2 - y1)

                    dist = hypot(pt.x - x3, pt.y - y3)
                    if not last_pt:
                        last_pt = pt
                        last_dist = dist
                    elif dist < last_dist:
                        last_dist = dist
                        last_pt = pt
        if last_pt:
            last_pt.x *= -1
            # pt = last_pt
            # Scene.canvas.create_oval(pt.x * Scene.unit - 5 + Scene.width//2, pt.y * Scene.unit - 5 + Scene.height//2, pt.x * Scene.unit + 5 + Scene.width//2, pt.y * Scene.unit + 5 + Scene.height//2, fill = 'yellow')
        
        return last_pt

raycaster = Raycast()
InputManager.initialisate()
def engine_update(update):
    time1 = time()

    for entity in Scene.all_entities:
        if entity.usable:
            entity.update()
    for ui_part in Scene.ui:
        ui_part.update()
        
    # pt = raycaster.ray(Vector(0, 1), Vector(0, -1))
    # Scene.canvas.create_oval(pt.x * Scene.unit - 5 + Scene.width//2, -pt.y * Scene.unit - 5 + Scene.height//2, pt.x * Scene.unit + 5 + Scene.width//2, -pt.y * Scene.unit + 5 + Scene.height//2, fill = 'yellow')
    
    update()

    time2 = time()
    Scene.tick(time1, time2, Scene.FPS)
    
    try:
        Scene.refresh()
    except:
        Scene.running = False