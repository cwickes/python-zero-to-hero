class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
    
    def volume(self):
        # V = (pi)(r^2)h
        return 3.14 * (self.radius ** 2) * self.height

    def surface_area(self):
        # A = 2(pi)(r)(r + h)
        return 2 * 3.14 * self.radius * (self.radius + self.height)

c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())